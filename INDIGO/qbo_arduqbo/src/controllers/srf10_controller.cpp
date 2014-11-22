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

#include <controllers/srf10_controller.h>



CDistanceSensor::CDistanceSensor(std::string name, uint8_t address, std::string topic, ros::NodeHandle& nh, std::string type, std::string frame_id) :
    name_(name), address_(address), nh_(nh), type_(type)
{



    cloud_.points.resize(1);
    cloud_.channels.resize(0);

    cloud_.header.frame_id=frame_id;
    cloud_.points[0].x=0;
    cloud_.points[0].y=0;
    cloud_.points[0].z=0;

    sensor_pub_ = nh.advertise<sensor_msgs::PointCloud>(topic, 1);
}

void CDistanceSensor::publish(unsigned int readValue, ros::Time time)
{
    float distance=0;
    if(type_.compare("srf10")==0)
    {
        distance=((float)readValue)/100;
    }
    else if(type_.compare("gp2d120")==0)
    {
        distance=(2914 / ((float)readValue + 5)) - 1;
    }
    else if(type_.compare("gp2d12")==0)
    {
        if (readValue<3)
            distance=-1;
        else
            distance=(6787.0 /((float)readValue - 3.0)) - 4.0;
    }
    else if(type_.compare("GP2Y0A21YK")==0)
    {
       distance = (12343.85 * pow((float)readValue,-1.15))/100.0;
    }
    
    cloud_.points[0].x=distance;
    cloud_.header.stamp=time;
    sensor_pub_.publish(cloud_);
}


std::string CDistanceSensor::getName()
{
    return name_;
}

void CSrf10Controller::createDistanceSensor(std::string paramName,std::string sensorName,std::string topic, ros::NodeHandle& nh){
 if(!nh.hasParam(paramName+"/address"))
        {
            ROS_WARN_STREAM("You need to set the address atribute for the sensor " << sensorName);
            return;
        }
        if(!nh.hasParam(paramName+"/type"))
        {
            ROS_WARN_STREAM("You need to set the type of the sensor " << sensorName);
            return;
        }

	int address;
        std::string type;
        std::string frame_id;
        std::string sensor_topic;
        double max_alert_distance;
        double min_alert_distance;

nh.getParam(paramName+"/address", address);
        nh.getParam(paramName+"/type", type);
        nh.param(paramName+"/frame_id", frame_id, std::string(""));
        nh.param(paramName+"/topic", sensor_topic, topic+"/"+sensorName);

if(!nh.hasParam(paramName+"/publish_if_obstacle"))
	nh.setParam(paramName+"/publish_if_obstacle", false);


 if (type.compare("srf10")==0)
        {
            srf10Sensors_[(uint8_t)address]=new CDistanceSensor(sensorName, (uint8_t)address, sensor_topic, nh, type, frame_id);
            srf10SensorsUpdateGroup_[(uint8_t)address]=1;
        }
        else if (type.compare("gp2d12")==0 || type.compare("gp2d120")==0 || type.compare("GP2Y0A21YK")==0)
        {
            adcSensors_[(uint8_t)address]=new CDistanceSensor(sensorName, (uint8_t)address, sensor_topic, nh, type, frame_id);
            adcSensorsAddresses_.push_back((uint8_t)address);
        }
        ROS_INFO_STREAM("Sensor " << sensorName << " of type " << type << " initialized");
}

CSrf10Controller::CSrf10Controller(std::string name, CQboduinoDriver *device_p, ros::NodeHandle& nh) :
    CController(name,device_p,nh)
{
    std::string topic;
    nh.param("controllers/"+name+"/topic", topic, std::string("srf10_state"));
    nh.param("controllers/"+name+"/rate", rate_, 15.0);
    if(nh.hasParam("controllers/"+name+"/sensors/front"))
    {
      std::map< std::string, XmlRpc::XmlRpcValue >::iterator it;
      std::map< std::string, XmlRpc::XmlRpcValue > value;
      XmlRpc::MyXmlRpcValue sensors;
      nh.getParam("controllers/"+name+"/sensors/front", sensors);
      ROS_ASSERT(sensors.getType() == XmlRpc::XmlRpcValue::TypeStruct);
      value=sensors;
      for(it=value.begin();it!=value.end();it++)
      {
        ROS_ASSERT((*it).second.getType() == XmlRpc::XmlRpcValue::TypeStruct);
        

	createDistanceSensor("controllers/"+name+"/sensors/front/"+(*it).first,(*it).first, topic, nh);

       
      }
    }
    if(nh.hasParam("controllers/"+name+"/sensors/back"))
    {
      std::map< std::string, XmlRpc::XmlRpcValue >::iterator it;
      std::map< std::string, XmlRpc::XmlRpcValue > value;
      XmlRpc::MyXmlRpcValue sensors;
      nh.getParam("controllers/"+name+"/sensors/back", sensors);
      ROS_ASSERT(sensors.getType() == XmlRpc::XmlRpcValue::TypeStruct);
      value=sensors;
      for(it=value.begin();it!=value.end();it++)
      {
        ROS_ASSERT((*it).second.getType() == XmlRpc::XmlRpcValue::TypeStruct);

createDistanceSensor("controllers/"+name+"/sensors/back/"+(*it).first,(*it).first, topic, nh);

      }
    }
    if(nh.hasParam("controllers/"+name+"/sensors/floor"))
    {
      std::map< std::string, XmlRpc::XmlRpcValue >::iterator it;
      std::map< std::string, XmlRpc::XmlRpcValue > value;
      XmlRpc::MyXmlRpcValue sensors;
      nh.getParam("controllers/"+name+"/sensors/floor", sensors);
      ROS_ASSERT(sensors.getType() == XmlRpc::XmlRpcValue::TypeStruct);
      value=sensors;
      for(it=value.begin();it!=value.end();it++)
      {
        ROS_ASSERT((*it).second.getType() == XmlRpc::XmlRpcValue::TypeStruct);
createDistanceSensor("controllers/"+name+"/sensors/floor/"+(*it).first,(*it).first, topic, nh);

      }
    }
    //config the sensors in the QBoard1
    int code=device_p_->setAutoupdateSensors(srf10SensorsUpdateGroup_);
    if (code<0)
        ROS_WARN("Unable to activate all srf10 sensors on the base control board");
    else
        ROS_INFO("All srf10 sensors of base control board correctly activated");
    timer_=nh.createTimer(ros::Duration(1/rate_),&CSrf10Controller::timerCallback,this);
}

CSrf10Controller::~CSrf10Controller()
{
    std::map< uint8_t,CDistanceSensor * >::iterator it;
    for (it=srf10Sensors_.begin();it!=srf10Sensors_.end();it++)
    {
      delete (*it).second;
    }
    srf10Sensors_.clear();
}

void CSrf10Controller::timerCallback(const ros::TimerEvent& e)
{
    ros::Time now=ros::Time::now();
    std::map<uint8_t,unsigned short> updatedDistances;
    int code=device_p_->getDistanceSensors(updatedDistances);
    if (code<0)
        ROS_ERROR("Unable to get srf10 sensor distances from the base control board");
    else
    {
        std::map< uint8_t,CDistanceSensor * >::iterator it;
        for (it=srf10Sensors_.begin();it!=srf10Sensors_.end();it++)
        {
            if (updatedDistances.count((*it).first)>0)
            {
                ROS_DEBUG_STREAM("Obtained distance " << updatedDistances[(*it).first] << " for srf10 sensor " << (*it).second->getName() << " from the base control board");

//do we publish al lvalues or only when we see something ? (0.0 values means no obstacle)
                bool publish_if_obstacle;

                nh.getParam("controllers/"+getName()+"/sensors/front/"+(*it).second->getName()+"/publish_if_obstacle", publish_if_obstacle);
                if( publish_if_obstacle){
                    if( updatedDistances[(*it).first]>0)
                       (*it).second->publish((float)updatedDistances[(*it).first],now);
}
                else{
                     (*it).second->publish((float)updatedDistances[(*it).first],now);
}
            }
            else
                ROS_WARN_STREAM("Could not obtain distance of srf10 sensor " << (int)((*it).first) << " from base control board");
        }
    }
    std::vector<unsigned int> adcReads;
    code=device_p_->getAdcReads(adcSensorsAddresses_,adcReads);
    if (code<0)
        ROS_ERROR("Unable to get adc sensor reads from the base control board");
    else
    {
        if(adcReads.size()!=adcSensorsAddresses_.size())
            ROS_ERROR("The asked addreses and the returned reads for the adc sensors do not match");
        else
        {
            for (int i=0;i<adcSensorsAddresses_.size();i++)
            {
                ROS_DEBUG_STREAM("Obtained distance " << adcReads[i] << " for adc sensor " << adcSensors_[adcSensorsAddresses_[i]]->getName() << " from the base control board");
                adcSensors_[adcSensorsAddresses_[i]]->publish(adcReads[i],now);
            }
        }
    }
}


std::set<uint8_t> CSrf10Controller::getConfiguredSrfs(void)
{
    std::set<uint8_t> configuredSrfs;
    std::map< uint8_t,CDistanceSensor * >::iterator it;
    for (it=srf10Sensors_.begin();it!=srf10Sensors_.end();it++)
    {
      configuredSrfs.insert((*it).first);
    }
    return configuredSrfs;
}
