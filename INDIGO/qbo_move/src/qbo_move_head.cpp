#include "ros/ros.h"

#include "std_srvs/Empty.h"
#include "qbo_arduqbo/motor_state.h"
#include "sensor_msgs/JointState.h"
#include "geometry_msgs/Point.h"
#include "geometry_msgs/PointStamped.h"

//pointer to nodeHandle so the callback can access to it too
ros::NodeHandle* n;

//publisher to move the head (to /cmd_joints)
ros::Publisher* move_head;

//variables for head PIDs
ros::Time timePreviousTilt;
int zeroTilt = 0;
double tiltRadPerTicks = 0;

  //tilt values to compute PID
double currentTilt = 0;
double previousTilt = 0;
double iTilt = 0;

int zeroPan = 0;
double panRadPerTicks = 0;

  //pan values to compute PID
double currentPan = 0;
double previousPan = 0;
double iPan = 0;



void initValues()
{
    //get the zero values (in ticks)
    n->getParam("/qbo_arduqbo/dynamixelservo/head_tilt_joint/neutral", zeroTilt);
    n->getParam("/qbo_arduqbo/dynamixelservo/head_pan_joint/neutral", zeroPan);

//get the range (in degrees) and the range (in ticks)
//compute the number of ticks per radians
    double range;
    n->getParam("/qbo_arduqbo/dynamixelservo/head_tilt_joint/range", range);
    int ticks;
    n->getParam("/qbo_arduqbo/dynamixelservo/head_tilt_joint/ticks", ticks);

    tiltRadPerTicks = range*M_PI/(ticks*180);

    n->getParam("/qbo_arduqbo/dynamixelservo/head_pan_joint/range", range);
    n->getParam("/qbo_arduqbo/dynamixelservo/head_pan_joint/ticks", ticks);

    panRadPerTicks = range*M_PI/(ticks*180);

//PID parameters as ROS params
   /* ros::param::set("/qbo_head_tracker/pan/kp", 0.35);
    ros::param::set("/qbo_head_tracker/pan/kd", 0.08);
    ros::param::set("/qbo_head_tracker/pan/ki", 0.01);
    ros::param::set("/qbo_head_tracker/tilt/kp", 0.6);
    ros::param::set("/qbo_head_tracker/tilt/kd", 0.07);
    ros::param::set("/qbo_head_tracker/tilt/ki", 0.005);*/

ros::param::set("/qbo_head_tracker/pan/kp", 0.1);
    ros::param::set("/qbo_head_tracker/pan/kd", 0.08);
    ros::param::set("/qbo_head_tracker/pan/ki", 0.01);
    ros::param::set("/qbo_head_tracker/tilt/kp", 0.3);
    ros::param::set("/qbo_head_tracker/tilt/kd", 0.07);
    ros::param::set("/qbo_head_tracker/tilt/ki", 0.005);

//last time we got a tilt value (used to compute differential factor of PID)
    timePreviousTilt = ros::Time::now();
}

//empty service to tell other nodes we are ready
bool isReadyService(std_srvs::Empty::Request  &req,
                    std_srvs::Empty::Response &res)
{
    return true;
}

//get the tilt position of the head and translate it into radians
void qboTiltCallback(const qbo_arduqbo::motor_state::ConstPtr& msg)
{
    currentTilt = (msg->position- zeroTilt)*tiltRadPerTicks;
}

//get the pan position of the head and translate it into radians
void qboPanCallback(const qbo_arduqbo::motor_state::ConstPtr& msg)
{
    currentPan = (msg->position- zeroPan)*panRadPerTicks;
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

//move the head to the absolute position (pan, tilt)
void moveHeadAbs(double pan, double tilt)
{
//ROS_INFO("Moving head at: [x: %lf, y: %lf]", pan, tilt);

//create JointState message
    sensor_msgs::JointState mvmt_msg;

    std::vector<std::string> names;
    names.push_back("head_pan_joint");
    names.push_back("head_tilt_joint");
    mvmt_msg.name = names;

    std::vector<double> position;
    position.push_back(pan);
    position.push_back(tilt);
    mvmt_msg.position = position;

//publish message
    move_head->publish(mvmt_msg);
}

//move the head at (pan, tilt) from its current position
void moveHeadRel(double pan, double tilt)
{
    /****** PID calculation for tilt ***********/
    double kp, kd, ki;
    ros::param::get("/qbo_head_tracker/tilt/kp", kp);
    ros::param::get("/qbo_head_tracker/tilt/kd", kd);
    ros::param::get("/qbo_head_tracker/tilt/ki", ki);

double  tiltPID = computePID(tilt, previousTilt, iTilt, timePreviousTilt, kp, ki, kd);

    /****** PID calculation for pan ***********/

    ros::param::get("/qbo_head_tracker/pan/kp", kp);
    ros::param::get("/qbo_head_tracker/pan/kd", kd);
    ros::param::get("/qbo_head_tracker/pan/ki", ki);

double  panPID = computePID(pan, previousPan, iPan, timePreviousTilt, kp, ki, kd);

//compute absolute position and use moveHeadAbs
    moveHeadAbs(currentPan + panPID, currentTilt + tiltPID);
//ROS_INFO("Moving head from: [x: %lf, y: %lf]", panPID, tiltPID);

    timePreviousTilt = ros::Time::now();
}

//move eyelids to (left, right) absolute position
void moveEyelidsAbs(double left, double right)
{
//create JointState message
    sensor_msgs::JointState mvmt_msg;

    std::vector<std::string> names;
    names.push_back("left_eyelid_joint");
    names.push_back("right_eyelid_joint");
    mvmt_msg.name = names;

    std::vector<double> position;
    position.push_back(left);
    position.push_back(right);
    mvmt_msg.position = position;

//  send message (same topic as the head)
    move_head->publish(mvmt_msg);
}

/**********
geometry_msgs::Point message :
(x, y) -> (pan, tilt)
z>0 -> absolute move, relative move otherwise
***********/
void qboMoveHeadCallback(const geometry_msgs::Point::ConstPtr& msg)
{
    // ROS_INFO("movement order: [pan: %lf, tilt: %lf]", msg->x, msg->y);

    if(msg->z > 0) //absolute move
    {
        moveHeadAbs(msg->x, msg->y);
    }
    else //relative move
    {
        moveHeadRel( msg->x,  msg->y);
    }
}


/**********
geometry_msgs::Point message :
(x, y) -> (left, right)
z unused
***********/
void qboMoveEyelidsCallback(const geometry_msgs::Point::ConstPtr& msg)
{
    //  ROS_INFO("eyelid order: [left: %lf, right: %lf]", msg->x, msg->y);
    moveEyelidsAbs(msg->x, msg->y);
}


/**********
geometry_msgs::PointStamped message :
stamp : unused at the moment
point.x = position in width in the image. In range [-1 (left), +1 (right)]
point.y = position in height in the image. In range [-1 (up), +1 (down)]
point.z : distance to object (unused if 0 or less)
***********/
void trackerCallback(const geometry_msgs::PointStamped::ConstPtr& msg)
{
    // ROS_INFO("tracker callback: [x: %lf, y: %lf, z: %lf]", msg->point.x, msg->point.y, msg->point.z);
if(msg->point.z > 0){
	double currentObjectPosX = msg->point.x;
	double currentObjectPosY = msg->point.y;
	double objectTargetX = 0.0; //TODO : read target position from parameters or from another callback
	double objectTargetY = 0.0;

    moveHeadRel(objectTargetX-currentObjectPosX , currentObjectPosY-objectTargetY );
	}

}



int main(int argc, char **argv)
{
//init node
    ros::init(argc, argv, "qbo_move_head");
    n = new ros::NodeHandle();

//wait for qbo_arduqbo node to be ready
    ros::service::waitForService("qbo_arduqbo/test_service", -1);

//initialize parameter values
    initValues();

/****
* Subscribers
****/
//subscribe to joint states to get the current position (in tilt)
    ros::Subscriber tilt_sub = n->subscribe("qbo_arduqbo/head_tilt_joint/state", 10, qboTiltCallback);
    ros::Subscriber pan_sub  =  n->subscribe("qbo_arduqbo/head_pan_joint/state", 10, qboPanCallback);

//subscribe to topics where someone asks the head to move
    ros::Subscriber move_head_sub  = n->subscribe("qbo_move_head", 10, qboMoveHeadCallback);
    ros::Subscriber move_eyelids_sub  = n->subscribe("qbo_move_eyelids", 10, qboMoveEyelidsCallback);
    ros::Subscriber tracker_sub  = n->subscribe("qbo_head_tracker", 10, trackerCallback);

/****
* Publisher
****/
//publisher to /cmd_joint to give orders to the motors through the qbo_arduqbo node
    ros::Publisher temp = n->advertise<sensor_msgs::JointState>("/cmd_joints", 10);
    move_head = &(temp);

    ROS_INFO("qbo_move_head node ready");
    ros::ServiceServer serviceReady = n->advertiseService("qbo_move_head/isReady", isReadyService);

//run until stopped
    ros::spin();
    return 0;
}
