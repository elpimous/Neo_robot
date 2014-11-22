/*
 * Software License Agreement (GPLv2 License)
 * 
 * Copyright (c) 2012 Thecorpora, Inc.
 *
 * This program is free software; you can redistribute it and/or 
 * modify it under the terms of the GNU General Public License as 
 * published by the Free Software Foundation; either version 2 of
 * the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of 
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
 * See the GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License 
 * along with this program; if not, write to the Free Software 
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, 
 * MA 02110-1301, USA.
 *
 * Authors: Miguel Angel Julian <miguel.a.j@openqbo.org>;
 * 
 */

#include <controllers/imu_controller.h>

static double gyro_measurement_scale = 0.07*3.14159/180;//sensitivity can be 0.07 or 0.0175 or 0.00875 and conversion degrees to radians

//accelerometer is in +- 2g mode, so sensibility is 18 mg/digit.
static double acc_measurement_scale = 0.018*9.81;

double calcAutoCovariance(int16_t *data, uint8_t data_length)
{
 //compute data mean
    double mean=0;
    for(uint8_t i=0;i<data_length;i++)
    {
        mean+=((double)data[i]);
    }
    mean = mean/data_length;


    double covariance = 0;
    for(uint8_t i=0;i<data_length;i++)
    {
	covariance+=((double)data[i]-mean)*gyro_measurement_scale*((double)data[i]-mean)*gyro_measurement_scale;
    }
    covariance = covariance/data_length;
    return covariance;
}

CImuController::CImuController(std::string name, CQboduinoDriver *device_p, ros::NodeHandle& nh) : CController(name,device_p,nh)
{


//zero values of the gyro to correct from drift
    gyroXzero_=0;
    gyroYzero_=0;
    gyroZzero_=0;

    is_calibrated_=false;
    imu_calibrated_.data=false;

    imu_msg_.header.frame_id = "base_link";

    //Orientation - all these values must be float
    imu_msg_.orientation.x = 0;
    imu_msg_.orientation.y = 0;
    imu_msg_.orientation.z = 0;
    imu_msg_.orientation.w = 1;

    boost::array<double, 9> orientation_covariance = {{-1., 0, 0,
                                                       0, -1., 0,
                                                        0, 0, -1.}};
    imu_msg_.orientation_covariance = orientation_covariance;

    //Angular velocity
    imu_msg_.angular_velocity.x = 0;
    imu_msg_.angular_velocity.y = 0;
    imu_msg_.angular_velocity.z = 0;

//where are this numbers from ?
    boost::array<double, 9> angular_velocity_covariance = {{0.008, 0, 0,
                                                            0, 0.008, 0,
                                                             0, 0, 0.008}};
    //boost::array<double, 9> angular_velocity_covariance = {{-1., 0, 0,
    //                                                   0, -1., 0,
    //                                                    0, 0, -1.}};

    imu_msg_.angular_velocity_covariance = angular_velocity_covariance;



    //Linear acceleration
    imu_msg_.linear_acceleration.x = 0;
    imu_msg_.linear_acceleration.y = 0;
    imu_msg_.linear_acceleration.z = 0;
//where are this numbers from ?
    boost::array<double, 9> linear_acceleration_covariance = {{0.002, 0, 0,
                                                               0, 0.002, 0,
                                                                0, 0, 0.002}};
    //boost::array<double, 9> linear_acceleration_covariance = {{-1., 0, 0,
    //                                                   0, -1., 0,
    //                                                    0, 0, -1.}};

    imu_msg_.linear_acceleration_covariance = linear_acceleration_covariance;

    std::string topic,imu_topic;
    nh.param("controllers/"+name+"/topic", imu_topic, std::string("imu_state"));
    nh.param("controllers/"+name+"/rate", rate_, 1.0);
   // nh.setParam("controllers/"+name+"/is_calibrated", is_calibrated_);
   // nh.setParam("controllers/"+getName()+"/last_calibrated", ros::Time::now().toSec());

    imu_pub_ = nh.advertise<sensor_msgs::Imu>(imu_topic+"/data", 1);

    calibrate_service_ = nh.advertiseService(imu_topic+"/calibrate", &CImuController::calibrateService,this);
    timer_=nh.createTimer(ros::Duration(1/rate_),&CImuController::timerCallback,this);
    calibrateMethod();
}

bool CImuController::calibrateMethod()
{
    ros::Rate r(rate_);
    int count=0;
    gyroXzero_=0;
    gyroYzero_=0;
    gyroZzero_=0;
    uint8_t calibrationTotalData=100;
    for(int i=0;i<calibrationTotalData;i++)
    {
        int16_t gyroX, gyroY, gyroZ;
        int8_t accelerometerX, accelerometerY, accelerometerZ;
        int code=device_p_->getIMU(gyroX,gyroY,gyroZ,accelerometerX,accelerometerY,accelerometerZ);
        if (code<0)
            ROS_ERROR("Unable to get IMU data from the base control board");
        else
        {
            ROS_DEBUG_STREAM("Obtained IMU data (" << (int)gyroX << "," << (int)gyroY << "," << (int)gyroZ << "," << (int)accelerometerX << "," << (int)accelerometerY << "," << (int)accelerometerZ << ") from the base control board ");

            gyroXzero_+=gyroX;
            gyroYzero_+=gyroY;
            gyroZzero_+=gyroZ;

            count++;
        }
        r.sleep();
    }

//we didn't get enough data, calibration failed
    if(count<calibrationTotalData*0.9)
    {
      is_calibrated_=false;
      gyroXzero_=0;
      gyroYzero_=0;
      gyroZzero_=0;
    }
    else
    {
      is_calibrated_=true;
      gyroXzero_/=count;
      gyroYzero_/=count;
      gyroZzero_/=count;
      
    }

    if(is_calibrated_)
        nh.setParam("controllers/"+getName()+"/last_calibrated", ros::Time::now().toSec());
    else
	nh.setParam("controllers/"+getName()+"/last_calibrated", -1);
    return is_calibrated_;

}

bool CImuController::calibrateService(std_srvs::Empty::Request &req, std_srvs::Empty::Response &res )
{
    return calibrateMethod();
}


void CImuController::timerCallback(const ros::TimerEvent& e)
{
    int16_t gyroX, gyroY, gyroZ;
    int8_t accelerometerX, accelerometerY, accelerometerZ;
    int code=device_p_->getIMU(gyroX,gyroY,gyroZ,accelerometerX,accelerometerY,accelerometerZ);
    if (code<0)
        ROS_ERROR("Unable to get IMU data from the base control board");
    else
    {
        //remove shift values 
        gyroX-=gyroXzero_;
        gyroY-=gyroYzero_;
        gyroZ-=gyroZzero_;
        ROS_DEBUG_STREAM("Obtained IMU data (" << (int)gyroX << "," << (int)gyroY << "," << (int)gyroZ << "," << (int)accelerometerX << "," << (int)accelerometerY << "," << (int)accelerometerZ << ") from the base control board ");

	//complete message
        imu_msg_.angular_velocity.x=((float)gyroZ)*gyro_measurement_scale;
        imu_msg_.angular_velocity.y=((float)gyroY)*gyro_measurement_scale;
        imu_msg_.angular_velocity.z=((float)gyroZ)*gyro_measurement_scale;


        imu_msg_.linear_acceleration.x=((float)accelerometerX)*acc_measurement_scale; 
        imu_msg_.linear_acceleration.y=((float)accelerometerY)*acc_measurement_scale;
        imu_msg_.linear_acceleration.z=((float)accelerometerZ)*acc_measurement_scale;

        imu_msg_.header.stamp = ros::Time::now();
        //publish
        imu_pub_.publish(imu_msg_);
    }
}
