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

#ifndef QBO_ARDUQBO_H_
#define QBO_ARDUQBO_H_

#include <map>
#include <vector>
#include <sstream>
#include <iostream>

#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
#include <ifaddrs.h>
#include <netinet/in.h>
#include <arpa/inet.h>

#include <ros/ros.h>
#include <ros/console.h>
#include <std_msgs/String.h>
#include "qbo_arduqbo/Test.h"
#include <sensor_msgs/JointState.h>

#include <driver/qboduino_driver.h>
#include <driver/arduqbo_instructions.h>
#include <servos.h>
#include <XmlRpcValue.h>
#include <myXmlRpc.h>
#include <dynamixel.h>


#include <controllers/controllers_class.h>
#include <controllers/base_controller.h>
#include <controllers/joint_controller.h>
#include <controllers/mouth_controller.h>
#include <controllers/nose_controller.h>
#include <controllers/battery_controller.h>
#include <controllers/mics_controller.h>
#include <controllers/srf10_controller.h>
#include <controllers/lcd_controller.h>
#include <controllers/imu_controller.h>


class CSerialController : public CQboduinoDriver
{
public:
  CSerialController(std::string port1="/dev/ttyUSB0", int baud1=115200, std::string port2="/dev/ttyUSB1", int baud2=115200, float timeout1=0.05, float timeout2=0.05, double rate=15, ros::NodeHandle nh=ros::NodeHandle("~"), std::string dmxPort="/dev/ttyUSB2");
  ~CSerialController();

  bool qboTestService(qbo_arduqbo::Test::Request  &req, qbo_arduqbo::Test::Response &res);

private:
  double rate_;
  ros::NodeHandle nh_;
  std::string dmxPort_;

  ros::Timer timer_;
  ros::Timer ipTimer_;

  std::map<std::string, CServo *> servosList_;
  std::vector<std::string> servosNamesList_;
  std::vector<CController *> controllersList_;
  CSrf10Controller* sensorsController_;

  ros::Publisher joint_pub_;

  void timerCallback(const ros::TimerEvent& e);
  void ipTimerCallback(const ros::TimerEvent& e);
  ros::ServiceServer qboTestService_;
};

#endif /* QBO_ARDUQBO_H_ */
