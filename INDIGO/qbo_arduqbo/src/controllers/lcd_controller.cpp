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

#include <controllers/lcd_controller.h>


CLCDController::CLCDController(std::string name, CQboduinoDriver *device_p, ros::NodeHandle& nh) : CController(name,device_p,nh)
{
    std::string topic;
    nh.param("controllers/"+name+"/topic", topic, std::string("cmd_lcd"));
    lcd_sub_ = nh.subscribe<std_msgs::String>(topic, 1, &CLCDController::setLCD,this);
    std::string hello;
    hello+="PC connected        ";
    device_p_->setLCD(hello);
}

void CLCDController::setLCD(const std_msgs::String::ConstPtr& msg)
{
    ROS_DEBUG_STREAM("LCD command arrived: " << msg->data);
    std::string content = msg->data;

//NOTE: there is a bug in the display (in QBoard1Firm/serialProtocol.cpp, L. 380)
//the usage of "333" and "                    " at the end try to by pass the bug
//but line L will have a max length of 20 - L


//first, we try to cut the content into 4 strings separated with /
    std::string delimiter= "/";
    std::string lines[4];
    int count = 0;

    for(int i = 0; i < 3; i++){
        int delIndex = content.find(delimiter);
        if(delIndex >= 0){
            lines[i] = content.substr(0, delIndex);
            lines[i] +="                    ";
            content = content.substr(delIndex+1);
            count ++;
        }
        else{
            break;
        }
    }

    if(count == 3){
//we have enough /, so write 1 string per line
        lines[3] = content+"                    ";
        int code=device_p_->setLCD(lines[0]);
        code=device_p_->setLCD('1'+lines[1]);
        code=device_p_->setLCD("22"+lines[2]);
        code=device_p_->setLCD("333"+lines[3]);
    }
    else{
        //old style message : line number is indicated by first character, with no character for line 0
        content = msg->data;


        if(content[0] == '2'){
            content = "2"+content; 
        }
        if(content[0] == '3'){
            content = "33"+content;
        }
        content +="                    "; 

        int code=device_p_->setLCD(content);
        if (code<0)
            ROS_ERROR_STREAM("Unable to send string \"" << content << "\" to the base control board");
        else
            ROS_DEBUG_STREAM("Sent string " << content << " to the base control board ");
    }
}
