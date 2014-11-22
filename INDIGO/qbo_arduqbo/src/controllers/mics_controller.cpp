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

#include <controllers/mics_controller.h>

CMicsController::CMicsController(std::string name, CQboduinoDriver *device_p, ros::NodeHandle& nh) : CController(name,device_p,nh)
{

    m0_=0;
    m1_=0;
    m2_=0;

    std::string mics_topic;
    nh.param("controllers/"+name+"/mics_topic", mics_topic, std::string("mics_state"));
    nh.param("controllers/"+name+"/rate", rate_, 1.0);
    mics_pub_ = nh.advertise<std_msgs::UInt16MultiArray>(mics_topic, 1);
    timer_=nh.createTimer(ros::Duration(1/rate_),&CMicsController::timerCallback,this);
}

void CMicsController::timerCallback(const ros::TimerEvent& e)
{
    int code=device_p_->getMics(m0_,m1_,m2_);
    if (code<0)
        ROS_ERROR("Unable to get mics levels from the head control board");
    else
    {
        ROS_DEBUG_STREAM("Obtained mics levels (" << (int)m0_ << "," << (int)m1_ << "," << (int)m2_ << ") from the head control board ");

	std_msgs::UInt16MultiArray msg;
	msg.data.push_back(m0_);
	msg.data.push_back(m1_);
	msg.data.push_back(m2_);
        //publish
        mics_pub_.publish(msg);
    }
}
