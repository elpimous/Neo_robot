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

#include <controllers/mouth_controller.h>

CMouthController::CMouthController(std::string name, CQboduinoDriver *device_p, ros::NodeHandle& nh) : CController(name,device_p,nh)
{
    std::string topic;
    nh.param("controllers/"+name+"/topic", topic, std::string("cmd_mouth"));
    //mouth_sub_ = nh.subscribe<qbo_arduqbo::Mouth>(topic, 1, &CMouthController::setMouth,this);
    mouth_sub_ = nh.subscribe<std_msgs::ByteMultiArray>(topic, 1, &CMouthController::setMouth,this);
}

void CMouthController::setMouth(const std_msgs::ByteMultiArray::ConstPtr& msg)
{
//rostopic pub -1 /cmd_mouth std_msgs/ByteMultiArray "{}" [0b0,0b0,0b10000,0b10100]
    if(msg->data.size() != 4){
        ROS_ERROR("Error : mouth command should contain 4 bytes");
        return;
    }
//mouth is commanded by 3 bytes, strangely arranged
    uint8_t b1,b2,b3;
    b1=(msg->data[0]&0b11111)<<1 | ((msg->data[1]&0b11)<<6);
    b2=(msg->data[1]&0b11100)>>2 | (msg->data[2]&0b11111)<<3;
    b3=msg->data[3]&0b11111;

    int code=device_p_->setMouth(b1, b2, b3);
    if (code<0)
        ROS_ERROR("Unable to send mouth to the head control board");
    else
    {
        ROS_DEBUG_STREAM("Mouth command sent");
    }
}

/*void CMouthController::setMouth(const qbo_arduqbo::Mouth::ConstPtr& msg)
{
    std::string debugStream = "Mouth command arrived: ";
    for(uint8_t i=0;i<20;i++)
    {
      debugStream += boost::lexical_cast<std::string>(msg->mouthImage[i]) + " ";
    }
    ROS_DEBUG_STREAM(debugStream);
    uint8_t b1,b2,b3;
    b1=0;
    b2=0;
    b3=0;
    for (uint8_t i=0;i<4;i++)
    {
        for (uint8_t j=0;j<5;j++)
        {
            uint8_t index=i*5+j;
            uint8_t ledIndex=i*5+4-j;
            if(index<7)
            {
              b1 |= ((msg->mouthImage[ledIndex]&0x01)<<(index+1));
            }
            else if(index<15)
            {
              b2 |= ((msg->mouthImage[ledIndex]&0x01)<<(index-7));
            }
            else
            {
              b3 |= ((msg->mouthImage[ledIndex]&0x01)<<(index-15));
            }
        }
    }
    int code=device_p_->setMouth(b1, b2, b3);
    if (code<0)
        ROS_ERROR("Unable to send mouth to the head control board");
    else
    {
        debugStream = "Sent mouth: ";
        for(uint8_t i=0;i<20;i++)
        {
          debugStream += boost::lexical_cast<std::string>(msg->mouthImage[i]) + " ";
        }
        debugStream += " to the head board ";
        ROS_DEBUG_STREAM(debugStream);
    }
}*/
