#include "ros/ros.h"

#include "std_srvs/Empty.h"
#include "geometry_msgs/Twist.h"
#include "geometry_msgs/Point.h"
#include "geometry_msgs/PointStamped.h"

//pointer to nodeHandle so the callback can access to it too
ros::NodeHandle* n;

//publisher to move the base (to /cmd_vel)
ros::Publisher* move_base;

ros::Time timePreviousBaseMove;
double previousLinear = 0;
double iLinear = 0;
double previousAngular = 0;
double iAngular = 0;

void initValues()
{ 
    ros::param::set("/qbo_base_tracker/base_linear/kp", 0.04);
    ros::param::set("/qbo_base_tracker/base_linear/kd",  0.04);
    ros::param::set("/qbo_base_tracker/base_linear/ki",  0.015);
    ros::param::set("/qbo_base_tracker/base_angular/kp",  0.6);
    ros::param::set("/qbo_base_tracker/base_angular/kd",  0.);
    ros::param::set("/qbo_base_tracker/base_angular/ki",  0.01);

timePreviousBaseMove = ros::Time::now();
}

//empty service to tell other nodes we are ready
bool isReadyService(std_srvs::Empty::Request  &req,
                    std_srvs::Empty::Response &res)
{
    return true;
}


double computePID(double value, double& previousValue, double& integralTerm, ros::Time previousTime, double kp, double ki, double kd){

//update integral term
integralTerm = 0.9*integralTerm + value;

//Derivative term
    ros::Time now = ros::Time::now();
    double derivativeTerm = (value - previousValue)/((now - previousTime).sec+0.001*(now - previousTime).nsec);

//update previous value
previousValue = value;
//don't update previous time as 1 time is use for pan and tilt

//perform PID
return kp*value+ki*integralTerm+kd*derivativeTerm;
}


void moveBase(double linear, double angular)
{
//send Twist message
    geometry_msgs::Twist mvmt_msg;
    mvmt_msg.linear.x = linear;
    mvmt_msg.linear.y = 0;
    mvmt_msg.linear.z = 0;
    mvmt_msg.angular.x = 0;
    mvmt_msg.angular.y = 0;
    mvmt_msg.angular.z = angular;

    move_base->publish(mvmt_msg);
}

void baseTracker(double linear, double angular)
{
    double kp, kd, ki;
    ros::param::get("/qbo_base_tracker/base_linear/kp", kp);
    ros::param::get("/qbo_base_tracker/base_linear/kd", kd);
    ros::param::get("/qbo_base_tracker/base_linear/ki", ki);

double  linearPID = computePID(linear, previousLinear, iLinear, timePreviousBaseMove, kp, ki, kd);

    ros::param::get("/qbo_base_tracker/base_angular/kp", kp);
    ros::param::get("/qbo_base_tracker/base_angular/kd", kd);
    ros::param::get("/qbo_base_tracker/base_angular/ki", ki);

double  angularPID = computePID(angular, previousAngular, iAngular, timePreviousBaseMove, kp, ki, kd);

//move the base
    moveBase(linearPID, angularPID);
//ROS_INFO("Moving base to: [linear: %lf, angular: %lf]", linearPID, angularPID);

    timePreviousBaseMove = ros::Time::now();

 /*   ros::Time now = ros::Time::now();
    ros::Duration timeSinceFloor = now - timePreviousFloorSeen ;

    if(timeSinceFloor.toSec() > MAX_TIME_FLOOR_DETECTION)
    {
        //we haven't seen the floor recently : we assume the robot may fall if going forward
        // ROS_INFO("No floor seen, I don't move");
        return;
    }*/

    /****** PID calculation for linear ***********/
/*
//Integral term
    iBaseLinear= 0.9*iBaseLinear+ forward;
    //Derivative term
    double dBaseLinear = (forward - previousBaseLinear)/((now - timePreviousBase).sec+0.001*(now - timePreviousBase).nsec);

//Parameters
    double kp;
    ros::param::get("/HR_tracker/base_linear/kp", kp);
    double kd;
    ros::param::get("/HR_tracker/base_linear/kd", kd);
    double ki;
    ros::param::get("/HR_tracker/base_linear/ki", ki);

    double  forwardPID = controlPID(forward, iBaseLinear, dBaseLinear, kp, kd, ki);

//If told not to move, don't move ! (you may be on a table...)
    if(forward == 0)
    {
        forwardPID = 0;
    }
*/
    /****** PID calculation for angular ***********/
/*
//Integral term
    iBaseAngular= 0.9*iBaseAngular+ pan;
    //Derivative term
    double dBaseAngular = (pan - previousBaseAngular)/((now - timePreviousBase).sec+0.001*(now - timePreviousBase).nsec);
//Parameters
    ros::param::get("/HR_tracker/base_angular/kp", kp);
    ros::param::get("/HR_tracker/base_angular/kd", kd);
    ros::param::get("/HR_tracker/base_angular/ki", ki);

    double  panPID = controlPID(pan, iBaseAngular, dBaseAngular, kp, kd, ki);

*/
    /******* obstacle avoidance part **********/

    //to test :)
   /* if(forwardPID != 0)
    {
        forwardPID = 0.4;
        panPID = 0;
    }*/


/*
    ros::Duration timeSinceRightObstacle = now - timePreviousRightObstacle ;

    bool recentRightValue = ((now - timePreviousRightObstacle ).toSec() < 1);
    bool recentLeftValue = ((now - timePreviousLeftObstacle ).toSec() < 1);

    double newForward = forwardPID;
    double newPan = panPID;
    double coefDistance = 0.6;
     double coefTurn = 0.8;

     double maxAngularSpeed = 0.8;

    double robotSize = 0.22;

    if(recentRightValue)
    {
        newForward = std::min(newForward, distRightObstacle*coefDistance  );
        if(distRightObstacle < 0.4){
        newForward = 0;
        }
        newPan = std::min(newPan, -0.1);
    }

    if(recentLeftValue)
    {
        newForward = std::min(newForward, distLeftObstacle*coefDistance  );
                if(distLeftObstacle < 0.4){
        newForward = 0;
        }
        newPan = std::max(newPan, 0.1);
    }

    if(recentLeftValue && recentRightValue)
    {
        newPan = coefTurn*atan2(robotSize, (distLeftObstacle - distRightObstacle));
        if(newPan > M_PI/2){
        newPan -= M_PI;
        }

        if(newPan > maxAngularSpeed)
        newPan = maxAngularSpeed;

                if(newPan < -maxAngularSpeed)
        newPan = -maxAngularSpeed;


    }

    if(newForward != forwardPID && newPan != panPID)
    {
        ROS_INFO("---------------------------------");
        ROS_INFO("movement before obstacle avoidance %lf,  %lf ", forwardPID, panPID);
        forwardPID = newForward;
        panPID = newPan;
        ROS_INFO("movement after obstacle avoidance %lf,  %lf ", forwardPID, panPID);
    }


//send Twist message
    geometry_msgs::Twist mvmt_msg;
    mvmt_msg.linear.x = forwardPID;
    mvmt_msg.linear.y = 0;
    mvmt_msg.linear.z = 0;
    mvmt_msg.angular.x = 0;
    mvmt_msg.angular.y = 0;
    mvmt_msg.angular.z = panPID;

    move_base->publish(mvmt_msg);*/
}



/**********
HR_move_base message :
linear
angular
***********/
void qboMoveBaseCallback(const geometry_msgs::Point::ConstPtr& msg)
{
    //  ROS_INFO("movement order: [linear: %lf, angular: %lf]", msg->linear, msg->angular);
    moveBase(msg->x, msg->y);

}

int main(int argc, char **argv)
{
//init node
    ros::init(argc, argv, "qbo_move_base");
    n = new ros::NodeHandle();

//wait for qbo_arduqbo node to be ready
    ros::service::waitForService("qbo_arduqbo/test_service", -1);

//initialize parameter values
    initValues();

ros::Subscriber move_base_sub  = n->subscribe("/qbo_move_base", 10, qboMoveBaseCallback);

    ros::Publisher temp = n->advertise<geometry_msgs::Twist>("/cmd_vel", 10);
    move_base = &(temp);

    ROS_INFO("qbo_move_base node ready");
    ros::ServiceServer serviceReady = n->advertiseService("/qbo_move_base/isReady", isReadyService);

//run until stopped
    ros::spin();
    return 0;
}
