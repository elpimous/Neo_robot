/* Auto-generated by genmsg_cpp for file /opt/ros/hydro/stacks/qbo_arduqbo/msg/motor_state.msg */
#ifndef QBO_ARDUQBO_MESSAGE_MOTOR_STATE_H
#define QBO_ARDUQBO_MESSAGE_MOTOR_STATE_H
#include <string>
#include <vector>
#include <map>
#include <ostream>
#include "ros/serialization.h"
#include "ros/builtin_message_traits.h"
#include "ros/message_operations.h"
#include "ros/time.h"

#include "ros/macros.h"

#include "ros/assert.h"

#include "std_msgs/Header.h"

namespace qbo_arduqbo
{
template <class ContainerAllocator>
struct motor_state_ {
  typedef motor_state_<ContainerAllocator> Type;

  motor_state_()
  : header()
  , id(0)
  , goal(0)
  , position(0)
  , error(0)
  , speed(0)
  , load(0.0)
  , voltage(0.0)
  , temperature(0)
  , moving(false)
  {
  }

  motor_state_(const ContainerAllocator& _alloc)
  : header(_alloc)
  , id(0)
  , goal(0)
  , position(0)
  , error(0)
  , speed(0)
  , load(0.0)
  , voltage(0.0)
  , temperature(0)
  , moving(false)
  {
  }

  typedef  ::std_msgs::Header_<ContainerAllocator>  _header_type;
   ::std_msgs::Header_<ContainerAllocator>  header;

  typedef int32_t _id_type;
  int32_t id;

  typedef int32_t _goal_type;
  int32_t goal;

  typedef int32_t _position_type;
  int32_t position;

  typedef int32_t _error_type;
  int32_t error;

  typedef int32_t _speed_type;
  int32_t speed;

  typedef double _load_type;
  double load;

  typedef double _voltage_type;
  double voltage;

  typedef int32_t _temperature_type;
  int32_t temperature;

  typedef uint8_t _moving_type;
  uint8_t moving;


  typedef boost::shared_ptr< ::qbo_arduqbo::motor_state_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::qbo_arduqbo::motor_state_<ContainerAllocator>  const> ConstPtr;
  boost::shared_ptr<std::map<std::string, std::string> > __connection_header;
}; // struct motor_state
typedef  ::qbo_arduqbo::motor_state_<std::allocator<void> > motor_state;

typedef boost::shared_ptr< ::qbo_arduqbo::motor_state> motor_statePtr;
typedef boost::shared_ptr< ::qbo_arduqbo::motor_state const> motor_stateConstPtr;


template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const  ::qbo_arduqbo::motor_state_<ContainerAllocator> & v)
{
  ros::message_operations::Printer< ::qbo_arduqbo::motor_state_<ContainerAllocator> >::stream(s, "", v);
  return s;}

} // namespace qbo_arduqbo

namespace ros
{
namespace message_traits
{
template<class ContainerAllocator> struct IsMessage< ::qbo_arduqbo::motor_state_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct IsMessage< ::qbo_arduqbo::motor_state_<ContainerAllocator>  const> : public TrueType {};
template<class ContainerAllocator>
struct MD5Sum< ::qbo_arduqbo::motor_state_<ContainerAllocator> > {
  static const char* value() 
  {
    return "7c778bda1190d2be2e7c5f3fad8d4eda";
  }

  static const char* value(const  ::qbo_arduqbo::motor_state_<ContainerAllocator> &) { return value(); } 
  static const uint64_t static_value1 = 0x7c778bda1190d2beULL;
  static const uint64_t static_value2 = 0x2e7c5f3fad8d4edaULL;
};

template<class ContainerAllocator>
struct DataType< ::qbo_arduqbo::motor_state_<ContainerAllocator> > {
  static const char* value() 
  {
    return "qbo_arduqbo/motor_state";
  }

  static const char* value(const  ::qbo_arduqbo::motor_state_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator>
struct Definition< ::qbo_arduqbo::motor_state_<ContainerAllocator> > {
  static const char* value() 
  {
    return "Header header\n\
int32 id            # motor id\n\
int32 goal          # commanded position (in encoder units)\n\
int32 position      # current position (in encoder units)\n\
int32 error         # difference between current and goal positions\n\
int32 speed         # current speed (0.111 rpm per unit)\n\
float64 load        # current load - ratio of applied torque over maximum torque\n\
float64 voltage     # current voltage (V)\n\
int32 temperature   # current temperature (degrees Celsius)\n\
bool moving         # whether the motor is currently in motion\n\
\n\
================================================================================\n\
MSG: std_msgs/Header\n\
# Standard metadata for higher-level stamped data types.\n\
# This is generally used to communicate timestamped data \n\
# in a particular coordinate frame.\n\
# \n\
# sequence ID: consecutively increasing ID \n\
uint32 seq\n\
#Two-integer timestamp that is expressed as:\n\
# * stamp.secs: seconds (stamp_secs) since epoch\n\
# * stamp.nsecs: nanoseconds since stamp_secs\n\
# time-handling sugar is provided by the client library\n\
time stamp\n\
#Frame this data is associated with\n\
# 0: no frame\n\
# 1: global frame\n\
string frame_id\n\
\n\
";
  }

  static const char* value(const  ::qbo_arduqbo::motor_state_<ContainerAllocator> &) { return value(); } 
};

template<class ContainerAllocator> struct HasHeader< ::qbo_arduqbo::motor_state_<ContainerAllocator> > : public TrueType {};
template<class ContainerAllocator> struct HasHeader< const ::qbo_arduqbo::motor_state_<ContainerAllocator> > : public TrueType {};
} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

template<class ContainerAllocator> struct Serializer< ::qbo_arduqbo::motor_state_<ContainerAllocator> >
{
  template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
  {
    stream.next(m.header);
    stream.next(m.id);
    stream.next(m.goal);
    stream.next(m.position);
    stream.next(m.error);
    stream.next(m.speed);
    stream.next(m.load);
    stream.next(m.voltage);
    stream.next(m.temperature);
    stream.next(m.moving);
  }

  ROS_DECLARE_ALLINONE_SERIALIZER;
}; // struct motor_state_
} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::qbo_arduqbo::motor_state_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const  ::qbo_arduqbo::motor_state_<ContainerAllocator> & v) 
  {
    s << indent << "header: ";
s << std::endl;
    Printer< ::std_msgs::Header_<ContainerAllocator> >::stream(s, indent + "  ", v.header);
    s << indent << "id: ";
    Printer<int32_t>::stream(s, indent + "  ", v.id);
    s << indent << "goal: ";
    Printer<int32_t>::stream(s, indent + "  ", v.goal);
    s << indent << "position: ";
    Printer<int32_t>::stream(s, indent + "  ", v.position);
    s << indent << "error: ";
    Printer<int32_t>::stream(s, indent + "  ", v.error);
    s << indent << "speed: ";
    Printer<int32_t>::stream(s, indent + "  ", v.speed);
    s << indent << "load: ";
    Printer<double>::stream(s, indent + "  ", v.load);
    s << indent << "voltage: ";
    Printer<double>::stream(s, indent + "  ", v.voltage);
    s << indent << "temperature: ";
    Printer<int32_t>::stream(s, indent + "  ", v.temperature);
    s << indent << "moving: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.moving);
  }
};


} // namespace message_operations
} // namespace ros

#endif // QBO_ARDUQBO_MESSAGE_MOTOR_STATE_H

