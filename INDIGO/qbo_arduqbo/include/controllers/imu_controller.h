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

#ifndef IMU_CONTROLLER_H
#define IMU_CONTROLLER_H

#include <driver/qboduino_driver.h>
#include <controllers/controllers_class.h>
#include "ros/ros.h"
#include <ros/console.h>
#include <sensor_msgs/Imu.h>
#include <std_msgs/Bool.h>
#include <std_srvs/Empty.h>

class CImuController : public CController
{
    public:
        CImuController(std::string name, CQboduinoDriver *device_p, ros::NodeHandle& nh);
        
    protected:
	ros::Publisher imu_pub_;

        int32_t gyroXzero_;
        int32_t gyroYzero_;
        int32_t gyroZzero_;

        bool is_calibrated_;
        sensor_msgs::Imu imu_msg_;
        std_msgs::Bool imu_calibrated_;
        ros::ServiceServer calibrate_service_;
        bool calibrateMethod();
        bool calibrateService(std_srvs::Empty::Request &req,
                              std_srvs::Empty::Response &res );
        void timerCallback(const ros::TimerEvent& e);
};

#endif
