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

#include <driver/qboduino_driver.h>

CQboduinoDriver::CQboduinoDriver(std::string port1, int baud1, std::string port2, int baud2, float timeout1, float timeout2) :
    firstDevice(), secondDevice(), timeout1_(timeout1*1000), timeout2_(timeout2*1000)
{
//open serial ports
    firstDevice.open(port1.c_str(),baud1);
    secondDevice.open(port2.c_str(),baud2);

    usleep(5500000);

//test what board is on port1 and read version
    if(!firstDevice.portOpen()) {
      std::cout << "Unable to open " << port1 << " port" << std::endl;
    }
    else
    {
        int board_id=-1, version=-1;
        boards_["first"]=&firstDevice;
        timeouts_["first"]=&timeout1_;
        int code = getVersion("first", board_id, version);
        if(code>=0 && board_id==0)//base control board
        {
            boards_["base"]=&firstDevice;
            timeouts_["base"]=&timeout1_;
            std::cout << "Base control board found in " << port1 << " and initialized at " << baud1 << " baudrate" << std::endl;
        }
        else if(code>=0 && board_id==1)//head control board
        {
            boards_["head"]=&firstDevice;
            timeouts_["head"]=&timeout1_;
            std::cout << "Head control board found in " << port1 << " and initialized at " << baud1 << " baudrate" << std::endl;
        }
        else
        {
          std::cout << "Device at " << port1 << " is not a Q.Board"<< std::endl;
        }
    }

//test what board is on port2 and read version
    if(!secondDevice.portOpen()) {
      std::cout << "Unable to open " << port2 << " port" << std::endl;
    }
    else
    {
        int board_id=-1, version=-1;
        boards_["second"]=&secondDevice;
        timeouts_["second"]=&timeout2_;
        int code = getVersion("second", board_id, version);
        if(code>=0 && board_id==0)//base control board
        {
            boards_["base"]=&secondDevice;
            timeouts_["base"]=&timeout2_;
            std::cout << "Base control board found in " << port2 << " and initialized at " << baud2 << " baudrate" << std::endl;
        }
        else if(code>=0 && board_id==1)//head control board
        {
            boards_["head"]=&secondDevice;
            timeouts_["head"]=&timeout2_;
            std::cout << "Head control board found in " << port2 << " and initialized at " << baud2 << " baudrate" << std::endl;;
        }
        else
        {
          std::cout << "Device at " << port2 << " is not a Q.Board"<< std::endl;
        }
    }
    if(boards_.count("base")==0 && boards_.count("head")==0)//no board found
      exit(-1);
}

//read data on the arduino
int CQboduinoDriver::read(cereal::CerealPort *port, std::string& read, long timeout)
{
    std::string buf;
    
    try
    {
        if(!port->readBetween(&buf,INPUT_FLAG,OUTPUT_FLAG,timeout))
        {
            return -1;
        }
    }
    catch(const std::exception & e)
    {
	std::cerr<<"qboduino driver : exception while trying to read" << e.what();
        return -1;
    }
    
//check if packet is correct
    int code=processResponse((uint8_t*)buf.c_str(),buf.size(),read);
 
  if( code != 1){
	read.clear();
    }

    return code;
}
        
int CQboduinoDriver::write(cereal::CerealPort *port, std::string& toWrite)
{
    std::string serialData;
    prepareData(toWrite, serialData);
    return port->write(serialData.c_str(),serialData.size());
}

int CQboduinoDriver::processResponse(uint8_t *buf, uint32_t length, std::string& read)
{
  read.clear();
  if (length<5) return -1; //packet too short
  if(buf[0]!=INPUT_FLAG) return -2; //bad first data
  if(buf[length-1]!=OUTPUT_FLAG) return -3; //bad last data
  uint8_t data[128];
  bool escapePressed=false;
  int currentDataIndex=0;
  for(uint32_t i=1;i<length-1;i++)
  {
//if escape is not pressed, put current buffer data in data table at index currentDataIndex
//if escape is pressed, add 2 to buffer data (but why ?)
//if buffer contain INPUT_SCAPE, escape is pressed
    if(escapePressed)
    {
      data[currentDataIndex]=buf[i]+2;
      escapePressed=false;
      currentDataIndex++;
    }
    else if(buf[i]==INPUT_SCAPE)
      escapePressed=true;
    else
    {
      data[currentDataIndex]=buf[i];
      escapePressed=false;
      currentDataIndex++;
    }
  }

//compute checksum
  uint8_t check=computeChecksum(data,currentDataIndex-1);
  uint8_t inCheck=data[currentDataIndex-1];
  if(check!=inCheck){
    return -4;
  }

//packet ok, put back into string
  for(int i=0;i<currentDataIndex-1;i++)
    read.push_back(data[i]);
  return 1;
}

void CQboduinoDriver::prepareData(std::string& toWrite, std::string& preparedData)
{
    preparedData.clear();
    preparedData.push_back(INPUT_FLAG);//add init data
        
    //compute and add checksum
    uint8_t check=computeChecksum((uint8_t *)toWrite.c_str(),(uint8_t)toWrite.size());
    toWrite.push_back((char)check);
    
    //copy everything from toWrite into preparedData
    // escape special characters
    for(unsigned int i=0;i<toWrite.size();i++)
    {
      if((uint8_t)toWrite[i]==INPUT_FLAG||(uint8_t)toWrite[i]==INPUT_SCAPE||(uint8_t)toWrite[i]==OUTPUT_FLAG)
      {
        preparedData.push_back(INPUT_SCAPE);
        preparedData.push_back(toWrite[i]-2);
      }
      else
      {
        preparedData.push_back(toWrite[i]);
      }
    }
    
    preparedData.push_back(OUTPUT_FLAG);//add end data
}

int CQboduinoDriver::lockAndSendCommand(std::string board, CComando& command, std::vector<dataUnion>& response, std::vector<dataUnion>& data)
{
    int code=-3;
    if(boards_.count(board)==0) return -2; //no board of that type detected

//lock mutex and send command to base
    if(board.compare("base")==0 && sending_data_mutex_.timed_lock(boost::posix_time::millisec(500)))
    {
        code=sendCommand(board,command,response,data);
        sending_data_mutex_.unlock();
        return code;
    }
    else
        code=-3; 

//lock mutex and send command to head
    if(board.compare("head")==0 && sending_data_head_mutex_.timed_lock(boost::posix_time::millisec(500)))
    {
        code=sendCommand(board,command,response,data);
        sending_data_head_mutex_.unlock();
        return code;
    }
    else
        code=-3;
    std::cout << "Mutex timeout" << std::endl;
    return code;
}

int CQboduinoDriver::sendCommand(std::string board, CComando& command, std::vector<dataUnion>& response, std::vector<dataUnion>& data)
{
    response.clear();
    cereal::CerealPort *port=boards_[board];
    long timeout=*timeouts_[board];
    port->flush();
    std::string oud;
    if(command.serialize(data, oud)<0)
        return -4; //data could not be serialized
    if(!write(port,oud))
        return -5; //data could not be writen on port
    std::string ind;
    if(!read(port,ind,timeout))
        return -6; //response could not be read
    if(command.deserialize(ind, response)<0)
    {
        return -7;//response could not be deserialized
    }
    return 1;
}
    
int CQboduinoDriver::getVersion(std::string board, int& board_number, int& version)
{
    CComando command=comandosSet_.version;
    std::vector<dataUnion> data, sent;
    int code=sendCommand(board,command,data,sent);

    if (code<0) return code;//error

    board_number=(int)data[0].b;
    version=(int)data[1].b;
    return code;
}
    
int CQboduinoDriver::setSpeed(float linear, float angular)
{
    dataUnion d;
//prepare the vector data containing 2 dataUnions (linear and angular)
    std::vector<dataUnion> data, resp;
    d.f=linear;
    data.push_back(d);
    d.f=angular;
    data.push_back(d);
    CComando command=comandosSet_.setSpeed;
    return (lockAndSendCommand("base",command,resp,data));
}

int CQboduinoDriver::setServo(uint8_t idx,unsigned short tics, unsigned short tics_per_second)
{
    dataUnion d;
//prepare the vector data containing 3 dataUnions (id, tics and tics per seconds)
    std::vector<dataUnion> data, resp;
    d.b=idx;
    data.push_back(d);
    d.h=tics;
    data.push_back(d);
    d.h=tics_per_second;
    data.push_back(d);
    CComando command=comandosSet_.setServo;
    return (lockAndSendCommand("head",command,resp,data));
}
    
int CQboduinoDriver::getOdometry(float& x, float& y, float& th)
{
    std::vector<dataUnion> data, sent;
    CComando command=comandosSet_.getOdometry;
    int code=lockAndSendCommand("base",command,data,sent);
    if (code<0) return code;//error
    x=data[0].f;
    y=data[1].f;
    th=data[2].f;
    return code;
}

int CQboduinoDriver::getServoPosition(uint8_t idx, unsigned short& tics)
{
    dataUnion d;
    std::vector<dataUnion> data,sent;
    d.b= idx;
    sent.push_back(d);
    CComando command=comandosSet_.getServo;
    int code=lockAndSendCommand("head",command,data,sent);
    if (code<0) return code;//error
    tics=data[0].h;
    return code;
}
int CQboduinoDriver::getHeadServosPositions(std::vector<unsigned short>& tics)
{
    dataUnion d;
    std::vector<dataUnion> data,sent;
    CComando command=comandosSet_.getHeadServos;
    int code=lockAndSendCommand("head",command,data,sent);
    if (code<0) return code;//error
    tics.push_back(data[0].h);
    tics.push_back(data[1].h);
    return code;
}
int CQboduinoDriver::getEyesServosPositions(std::vector<unsigned short>& tics)
{
    dataUnion d;
    std::vector<dataUnion> data,sent;
    CComando command=comandosSet_.getEyeServos;
    int code=lockAndSendCommand("head",command,data,sent);
    if (code<0) return code;
    tics.push_back(data[0].h);
    tics.push_back(data[1].h);
    return code;
}
int CQboduinoDriver::setMouth(uint8_t b0, uint8_t b1, uint8_t b2)
{
    dataUnion d;
    std::vector<dataUnion> data,resp;
    d.b= b0;
    data.push_back(d);
    d.b= b1;
    data.push_back(d);
    d.b= b2;
    data.push_back(d);
    
    CComando command=comandosSet_.mouth;
    return (lockAndSendCommand("head",command,resp,data));
}

int CQboduinoDriver::setNose(uint8_t nose)
{
      dataUnion d;
      std::vector<dataUnion> data,resp;
      d.b= nose;
      data.push_back(d);

      CComando command=comandosSet_.nose;
      return (lockAndSendCommand("head",command,resp,data));
}

int CQboduinoDriver::setLCD(std::string msg)
{
    dataUnion d;
    std::vector<dataUnion> data,resp;
    d.s= msg;
    data.push_back(d);
    
    CComando command=comandosSet_.lcd;
    return (lockAndSendCommand("base",command,resp,data));
}

int CQboduinoDriver::getBattery(float& level, uint8_t& stat)
{
    std::vector<dataUnion> data,sent;
    
    CComando command=comandosSet_.battery;
    int code=lockAndSendCommand("base",command,data,sent);
    if (code<0) return code;//error
//get battery level and QBO state
    level=((float)data[0].b);
    stat=((uint8_t)data[1].b);
    return code;
}

int CQboduinoDriver::getMics(uint16_t& m0,uint16_t& m1,uint16_t& m2)
{
    std::vector<dataUnion> data,sent;
    
    CComando command=comandosSet_.getMics;
    int code=lockAndSendCommand("head",command,data,sent);
    if (code<0) return code;//error
    m0=(uint16_t)data[0].h;
    m1=(uint16_t)data[1].h;
    m2=(uint16_t)data[2].h;
    return code;
}

int CQboduinoDriver::setMic(uint8_t mic)
{
    dataUnion d;
    std::vector<dataUnion> data,resp;
    d.b=mic;
    data.push_back(d);
    
    CComando command=comandosSet_.setMic;
    return (lockAndSendCommand("head",command,resp,data));
}

int CQboduinoDriver::setAutoupdateSensors(std::map<uint8_t,uint8_t> sensors)
{
    dataUnion d;
    std::vector<dataUnion> data,resp;
    std::map< uint8_t,uint8_t >::iterator it;
    for(it=sensors.begin();it!=sensors.end();it++)
    {
      d.b=(*it).first;
      data.push_back(d);
      d.b=(*it).second;
      data.push_back(d);
    }
    
    CComando command=comandosSet_.setAutoupdateSensors;
    return (lockAndSendCommand("base",command,resp,data));
}
int CQboduinoDriver::getDistanceSensors(std::map<uint8_t,unsigned short>& sensorsDistances)
{
    dataUnion d;
    std::vector<dataUnion> data,sent;
    sensorsDistances.clear();
    
    CComando command=comandosSet_.distanceSensors;
    int code=lockAndSendCommand("base",command,data,sent);
    if (code<0) return code;//error
    for (unsigned int i=0;i<data.size()/2;i++)
    {
      sensorsDistances[data[2*i].b]=data[2*i+1].h;
    }
    return code;
}

int CQboduinoDriver::getAdcReads(std::vector<uint8_t> addresses, std::vector<unsigned int>& readValues)
{
    dataUnion d;
    std::vector<dataUnion> received,sent;
    readValues.clear();
    if(addresses.size()==0)
      return 1;
    for(int i=0;i<addresses.size();i++)
    {
      d.b=addresses[i];
      sent.push_back(d);
    }
    
    CComando command=comandosSet_.adcReads;
    int code=lockAndSendCommand("base",command,received,sent);
    if (code<0) return code;//error
    for (unsigned int i=0;i<received.size();i++)
    {
      readValues.push_back(received[i].h);
    }
    return code;
  
}

int CQboduinoDriver::getIMU(int16_t& gyroX,int16_t& gyroY,int16_t& gyroZ,int8_t& accelerometerX,int8_t& accelerometerY,int8_t& accelerometerZ)
{
    std::vector<dataUnion> data,sent;

    CComando command=comandosSet_.getIMU;
    int code=lockAndSendCommand("base",command,data,sent);
    if (code<0) return code;//error
    gyroX=(int16_t)data[0].h;
    gyroY=(int16_t)data[1].h;
    gyroZ=(int16_t)data[2].h;
    accelerometerX=(int8_t)data[3].b;
    accelerometerY=(int8_t)data[4].b;
    accelerometerZ=(int8_t)data[5].b;
    return code;
}

int CQboduinoDriver::resetStall()
{
    std::vector<dataUnion> data,sent;

    CComando command=comandosSet_.resetStall;
    int code=lockAndSendCommand("base",command,data,sent);
    return code;
}

int CQboduinoDriver::getMotorsState(uint8_t& state)
{
    std::vector<dataUnion> data,sent;

    CComando command=comandosSet_.getMotorsState;
    int code=lockAndSendCommand("base",command,data,sent);
    if (code<0) return code;//error
    state=(uint8_t)data[0].b;
    return code;
}

int CQboduinoDriver::getIRs(uint8_t& ir0,uint8_t& ir1,uint8_t& ir2)
{
    std::vector<dataUnion> data,sent;

    CComando command=comandosSet_.baseInfraRed;
    int code=lockAndSendCommand("base",command,data,sent);
    if (code<0) return code;//error
    ir0=(uint16_t)data[0].b;
    ir1=(uint16_t)data[1].b;
    ir2=(uint16_t)data[2].b;
    return code;
}

int CQboduinoDriver::getI2cDevicesState(uint8_t& state)
{
    std::vector<dataUnion> data,sent;

    CComando command=comandosSet_.getI2cDevicesState;
    int code=lockAndSendCommand("base",command,data,sent);
    if (code<0) return code;//error
    state=(uint16_t)data[0].b;
    return code;
}

uint8_t computeChecksum(uint8_t *key, uint8_t len)
{
  uint8_t hash=0;
  for (uint8_t i=0; i<len; i++)
  {
    hash = checksumdata[hash^key[i]];
  }
  return (hash);
}
