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

#ifndef SRF10_CONTROLLER_H
#define SRF10_CONTROLLER_H

#include <driver/qboduino_driver.h>
#include <controllers/controllers_class.h>
#include "ros/ros.h"
#include <ros/console.h>
#include <map>
#include <vector>
#include <set>
#include <sensor_msgs/PointCloud.h>

#include <myXmlRpc.h>



class CDistanceSensor
{
    public:
        CDistanceSensor(std::string name, uint8_t address, std::string topic, ros::NodeHandle& nh, std::string type, std::string frame_id="");
        void publish(unsigned int readedValue, ros::Time time);

        std::string getName();

    protected:
        std::string name_;
        uint8_t address_;
	std::string type_;
        ros::NodeHandle nh_;
	ros::Publisher sensor_pub_;

        sensor_msgs::PointCloud cloud_;

};

class CSrf10Controller : public CController
{
    public:
        CSrf10Controller(std::string name, CQboduinoDriver *device_p, ros::NodeHandle& nh);
        std::set<uint8_t> getConfiguredSrfs(void);
        ~CSrf10Controller();

    protected:
        void timerCallback(const ros::TimerEvent& e);
        std::map<uint8_t,CDistanceSensor *> srf10Sensors_;
        std::map<uint8_t,uint8_t> srf10SensorsUpdateGroup_;
        std::map<uint8_t,CDistanceSensor *> adcSensors_;
        std::vector<uint8_t> adcSensorsAddresses_;
	void createDistanceSensor(std::string paramName,std::string sensorName,std::string topic, ros::NodeHandle& nh);
};

#endif
