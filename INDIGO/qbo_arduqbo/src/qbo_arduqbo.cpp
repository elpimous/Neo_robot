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

#include <qbo_arduqbo.h>


CSerialController::CSerialController(std::string port1, int baud1, std::string port2, int baud2, float timeout1, float timeout2, double rate, ros::NodeHandle nh, std::string dmxPort) :
  CQboduinoDriver(port1, baud1, port2, baud2, timeout1, timeout2), rate_(rate), nh_(nh), dmxPort_(dmxPort)
{
  //Check parameters in ROS_PARAM and start controllers
  //Advertise the test service
  qboTestService_=nh_.advertiseService("/qbo_arduqbo/test_service", &CSerialController::qboTestService, this);

    //Initialize and create object for all controlled servos
    if(nh_.hasParam("controlledservos"))
    {
      std::map< std::string, XmlRpc::XmlRpcValue >::iterator it;
      std::map< std::string, XmlRpc::XmlRpcValue > value;
      XmlRpc::MyXmlRpcValue servos;
      nh_.getParam("controlledservos", servos);
      ROS_ASSERT(servos.getType() == XmlRpc::XmlRpcValue::TypeStruct);
      value=servos;
      for(it=value.begin();it!=value.end();it++)
      {
        ROS_ASSERT((*it).second.getType() == XmlRpc::XmlRpcValue::TypeStruct);
        servosList_[(*it).first]=new ControledServo((*it).first,this);
        servosNamesList_.push_back((*it).first);
        //Set servos parameters
        servosList_[(*it).first]->setParams((*it).second);
        servosList_[(*it).first]->setAngle(0);
        ROS_INFO_STREAM("Controlled servo " << (*it).first << " started");
      }
    }
    //Initialize and create object for all Un-controlled servos
    if(nh_.hasParam("uncontrolledservos"))
    {
      std::map< std::string, XmlRpc::XmlRpcValue >::iterator it;
      std::map< std::string, XmlRpc::XmlRpcValue > value;
      XmlRpc::MyXmlRpcValue servos;
      nh_.getParam("uncontrolledservos", servos);
      ROS_ASSERT(servos.getType() == XmlRpc::XmlRpcValue::TypeStruct);
      value=servos;
      for(it=value.begin();it!=value.end();it++)
      {
        ROS_ASSERT((*it).second.getType() == XmlRpc::XmlRpcValue::TypeStruct);
        servosList_[(*it).first]=new CServo((*it).first,this);
        servosNamesList_.push_back((*it).first);
        //Set servos parameters
        servosList_[(*it).first]->setParams((*it).second);
        servosList_[(*it).first]->setAngle(0);
        ROS_INFO_STREAM("Uncontrolled servo " << (*it).first << " started");
      }
    }
//Initialize and create object for all dynamixel servos
    if(nh_.hasParam("dynamixelservo"))
    {
      //Start dynamixel port
      if( dxl_initialize(const_cast<char *>(dmxPort_.c_str()), 1) == 0 )
      {
          ROS_ERROR( "Failed to open dynamixel controller!\n" );
      }
      else
      {
          ROS_INFO( "Succeed to open dynamixel controller!\n" );
          std::map< std::string, XmlRpc::XmlRpcValue >::iterator it;
          std::map< std::string, XmlRpc::XmlRpcValue > value;
          XmlRpc::MyXmlRpcValue servos;
          nh_.getParam("dynamixelservo", servos);
          ROS_ASSERT(servos.getType() == XmlRpc::XmlRpcValue::TypeStruct);
          value=servos;
          for(it=value.begin();it!=value.end();it++)
          {
            ROS_ASSERT((*it).second.getType() == XmlRpc::XmlRpcValue::TypeStruct);
            servosList_[(*it).first]=new DynamixelServo(nh,(*it).first,this);
            servosNamesList_.push_back((*it).first);
            //Set servos parameters
            ((DynamixelServo*)servosList_[(*it).first])->changeTorque(254);
            servosList_[(*it).first]->setParams((*it).second);
            servosList_[(*it).first]->setAngle(0,0.3);
            ROS_INFO_STREAM("Dynamixel servo " << (*it).first << " started");
          }
      }
    }
    //Check for controllers
    if(nh_.hasParam("controllers"))
    {
      std::map< std::string, XmlRpc::XmlRpcValue >::iterator it;
      std::map< std::string, XmlRpc::XmlRpcValue > value;
      XmlRpc::MyXmlRpcValue controllers;
      nh_.getParam("controllers", controllers);
      ROS_ASSERT(controllers.getType() == XmlRpc::XmlRpcValue::TypeStruct);
      value=controllers;
      for(it=value.begin();it!=value.end();it++)
      {
        ROS_ASSERT((*it).second.getType() == XmlRpc::XmlRpcValue::TypeStruct);
        XmlRpc::XmlRpcValue controller_params=(*it).second;
        if(controller_params.hasMember("type"))
        {
          std::string type=controller_params["type"];
          //Joint controller
          if(type.compare("joint_controller")==0)
          {
            ROS_INFO("joint_controller started");
            controllersList_.push_back(new CJointController((*it).first, this, nh, servosList_));
          }
          //Mouth controller
          else if(type.compare("mouth_controller")==0)
          {
            ROS_INFO("mouth_controller started");
            controllersList_.push_back(new CMouthController((*it).first, this, nh));
          }
          else if(type.compare("nose_controller")==0)
          {
            ROS_INFO("nose_controller started");
            controllersList_.push_back(new CNoseController((*it).first, this, nh));
          }
          else if(type.compare("mics_controller")==0)
          {
            ROS_INFO("mics_controller started");
            controllersList_.push_back(new CMicsController((*it).first, this, nh));
          }
	  else if(type.compare("base_controller")==0)
          {
            ROS_INFO("base_controller started");
            controllersList_.push_back(new CBaseController((*it).first, this, nh));
          }
          //Battery controller
          else if(type.compare("battery_controller")==0)
          {
            ROS_INFO("battery_controller started");
            controllersList_.push_back(new CBatteryController((*it).first, this, nh));
          }
          //Sensors controller (I2C sonar sensors and ADC readings)
          else if(type.compare("sensors_controller")==0)
          {
            ROS_INFO("sensors_controller started");
            sensorsController_ = new CSrf10Controller((*it).first, this, nh);
            controllersList_.push_back(sensorsController_);
          }
          //Back LCD controller
          else if(type.compare("lcd_controller")==0)
          {
            ROS_INFO("lcd_controller started");
            controllersList_.push_back(new CLCDController((*it).first, this, nh));
            ipTimer_=nh_.createTimer(ros::Duration(5),&CSerialController::ipTimerCallback,this);
          }
          //IMU board controller
          else if(type.compare("imu_controller")==0)
          {
            ROS_INFO("imu_controller started");
            controllersList_.push_back(new CImuController((*it).first, this, nh));
          }
        }
      }
    }
    //The following lines setup the joint state publisher at the given rate
    std::string topic;
    nh_.param("joint_states_topic", topic, std::string("joint_states"));
    joint_pub_ = nh_.advertise<sensor_msgs::JointState>(topic, 1);
    timer_=nh_.createTimer(ros::Duration(1/rate_),&CSerialController::timerCallback,this);

}

CSerialController::~CSerialController()
{
  std::string goodbye;
  //goodbye.push_back(12);        //Code that cleans the LCD screen
  goodbye+="Waiting for PC        ";
  this->setLCD(goodbye);
  
  std::map< std::string, CServo * >::iterator it;
  for (it=servosList_.begin();it!=servosList_.end();it++)
  {
    delete (*it).second;
  }
  servosList_.clear();
  while(controllersList_.size()>0)
  {
    delete controllersList_.back();
    controllersList_.pop_back();
  }
  sensorsController_=NULL;
}

//publish the states of the servos
void CSerialController::timerCallback(const ros::TimerEvent& e) {
  sensor_msgs::JointState joint_state;
  int servos_count=servosList_.size();
  for(int i=0;i<servos_count;i++)
  {
    float angle=servosList_[servosNamesList_[i]]->getAngle();
    if(angle!=-1000)
    {
        joint_state.name.push_back(servosNamesList_[i]);
        joint_state.position.push_back(angle);
        joint_state.velocity.push_back(0);
    }
  }
  joint_state.header.stamp = ros::Time::now();
  //publish
  joint_pub_.publish(joint_state);
}

bool sendHostname=true;
void CSerialController::ipTimerCallback(const ros::TimerEvent& e)
{
  struct ifaddrs * ifAddrStruct=NULL;
  struct ifaddrs * ifa=NULL;
  void * tmpAddrPtr=NULL;

  getifaddrs(&ifAddrStruct);
  bool ip_found=false;

  setLCD(std::string("PC connected        "));


  if(sendHostname)
  {
    char hostname[40];
    unsigned int hostnameLen=40;
  
    gethostname(hostname,hostnameLen);
    //printf("Hostname: %s\n",hostname);
    std::string host_string("1H: ");
    host_string+=std::string(hostname)+"                   ";
    setLCD(host_string);
  }
  else
  {
    for (ifa = ifAddrStruct; ifa != NULL; ifa = ifa->ifa_next)
    {
      if (ifa ->ifa_addr->sa_family==AF_INET)
      { // check it is IP4
        // is a valid IP4 Address
        tmpAddrPtr=&((struct sockaddr_in *)ifa->ifa_addr)->sin_addr;
        char addressBuffer[INET_ADDRSTRLEN];
        inet_ntop(AF_INET, tmpAddrPtr, addressBuffer, INET_ADDRSTRLEN);
        std::string ip_string;
        if(strncmp(ifa->ifa_name,"eth",3)==0 || strncmp(ifa->ifa_name,"wlan",4)==0 || strncmp(ifa->ifa_name,"ath",3)==0)
        {
          //printf("%s IP Address %s\n", ifa->ifa_name, addressBuffer);
          ip_string="1IP: "+std::string(addressBuffer)+"        ";
          setLCD(ip_string);
          ip_found=true;
          break;
        }
      }
    }
    if(!ip_found)
    {
      setLCD(std::string("1IP: Not connected    "));
    }
  }
  if (ifAddrStruct!=NULL) freeifaddrs(ifAddrStruct);
  sendHostname=!sendHostname;
}

bool CSerialController::qboTestService(qbo_arduqbo::Test::Request  &req, qbo_arduqbo::Test::Response &res)
{
  //qboard1 state
  if(boards_.count("base")==1)
  {
    res.Qboard1=true;

    //get distances from all distance sensors
    std::set<uint8_t> configuredSrfs = sensorsController_->getConfiguredSrfs();
    std::map<uint8_t,unsigned short> sensorsDistances;
    getDistanceSensors(sensorsDistances);

    //add all configured SRF in the res.SRFAddress vector
    std::map<uint8_t,unsigned short>::iterator p;
    uint8_t i=0;
    res.SRFAddress.clear();
    for(p = sensorsDistances.begin(); p != sensorsDistances.end(); p++)
    {
      res.SRFAddress.push_back(p->first);
      i++;
      if(configuredSrfs.count(p->first)>0)
      {
          configuredSrfs.erase(p->first);
      }
    }
    res.SRFcount=i;

    //all SRF remaining in configured SRF have not given a result through getSensorDistances
    //put them in res.SRFNotFound vector
    std::set<uint8_t>::iterator setIt;
    res.SRFNotFound.clear();
    for(setIt = configuredSrfs.begin(); setIt != configuredSrfs.end(); setIt++)
    {
        res.SRFNotFound.push_back(*setIt);
    }

    //test devices communicating through I2C
    uint8_t I2cDevicesState=0;
    uint8_t motorsState=0;
    getI2cDevicesState(I2cDevicesState);
    getMotorsState(motorsState);
    res.Gyroscope=I2cDevicesState&0x01;
    res.Accelerometer=I2cDevicesState&0x02;
    res.LCD=I2cDevicesState&0x04;
    res.Qboard3=I2cDevicesState&0x08;
    res.rightMotor=motorsState&0x01;
    res.leftMotor=motorsState&0x02;
  }
  else
  {
    res.Qboard1=true; // why do we set this to true if the board is not found ?
    res.SRFcount=0;
    res.Gyroscope=false;
    res.Accelerometer=false;
    res.LCD=false;
    res.Qboard3=false;
  }
  //qboard2 state
  if(boards_.count("head")==1)
    res.Qboard2=true;
  else
    res.Qboard2=false;

  return true;
}

//main : read param for baud, port, timeout
//then start serial_controller
//then spin
int main(int argc, char** argv)
{
  ros::init(argc, argv, "serial_comm_node");
  ros::NodeHandle n("~");
  std::string port1,port2,dmxPort;
  int baud1,baud2;
  double timeout1,timeout2,rate;
  //Read serial port configuration
  n.param("port1", port1, std::string("/dev/ttyUSB0"));
  std::cout << port1 << std::endl;
  n.param("port2", port2, std::string("/dev/ttyUSB1"));
  std::cout << port2 << std::endl;
  n.param("baud1", baud1, 115200);
  n.param("baud2", baud2, 115200);
  n.param("timeout1", timeout1, 0.01);
  n.param("timeout2", timeout2, 0.01);
  //Read joint state publishing rate
  n.param("rate", rate, 15.0);
  n.param("dmxPort", dmxPort, std::string("/dev/ttyUSB2"));
  CSerialController serial_controller(port1,baud1,port2,baud2,timeout1,timeout2,rate,n,dmxPort);
  ROS_INFO("Ready to send messages to the QBoards.");
  ros::spin();

  return 0;
}

