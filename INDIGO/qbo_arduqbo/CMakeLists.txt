cmake_minimum_required(VERSION 2.8.3)
project(qbo_arduqbo)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  tf
  message_generation
)

## System dependencies are found with CMake's conventions
# find_package(Boost REQUIRED COMPONENTS system)


## Uncomment this if the package has a setup.py. This macro ensures
## modules and global scripts declared therein get installed
## See http://ros.org/doc/api/catkin/html/user_guide/setup_dot_py.html
# catkin_python_setup()

################################################
## Declare ROS messages, services and actions ##
################################################

## To declare and build messages, services or actions from within this
## package, follow these steps:
## * Let MSG_DEP_SET be the set of packages whose message types you use in
##   your messages/services/actions (e.g. std_msgs, actionlib_msgs, ...).
## * In the file package.xml:
##   * add a build_depend and a run_depend tag for each package in MSG_DEP_SET
##   * If MSG_DEP_SET isn't empty the following dependencies might have been
##     pulled in transitively but can be declared for certainty nonetheless:
##     * add a build_depend tag for "message_generation"
##     * add a run_depend tag for "message_runtime"
## * In this file (CMakeLists.txt):
##   * add "message_generation" and every package in MSG_DEP_SET to
##     find_package(catkin REQUIRED COMPONENTS ...)
##   * add "message_runtime" and every package in MSG_DEP_SET to
##     catkin_package(CATKIN_DEPENDS ...)
##   * uncomment the add_*_files sections below as needed
##     and list every .msg/.srv/.action file to be processed
##   * uncomment the generate_messages entry below
##   * add every package in MSG_DEP_SET to generate_messages(DEPENDENCIES ...)

## Generate messages in the 'msg' folder
 add_message_files(
   FILES
   LCD.msg
   Mouth.msg
   Nose.msg
   BatteryLevel.msg
   motor_state.msg
   Irs.msg
   NoiseLevels.msg
 )

## Generate services in the 'srv' folder
 add_service_files(
   FILES
   BaseStop.srv
   TorqueEnable.srv
   Test.srv
 )

## Generate actions in the 'action' folder
# add_action_files(
#   FILES
#   Action1.action
#   Action2.action
# )

## Generate added messages and services with any dependencies listed here
 generate_messages(
   DEPENDENCIES
   std_msgs
 )

###################################
## catkin specific configuration ##
###################################
## The catkin_package macro generates cmake config files for your package
## Declare things to be passed to dependent projects
## INCLUDE_DIRS: uncomment this if you package contains header files
## LIBRARIES: libraries you create in this project that dependent projects also need
## CATKIN_DEPENDS: catkin_packages dependent projects also need
## DEPENDS: system dependencies of this project that dependent projects also need
catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES qbo_arduqbo
  CATKIN_DEPENDS roscpp rospy std_msgs tf message_runtime
#  DEPENDS system_lib
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
 include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_library(cereal_port src/cereal_port/CerealPort.cpp)


add_library(libdxl src/dynamixel_sdk/src/dxl_hal.c)
add_library(dynamixel src/dynamixel_sdk/src/dynamixel.c)
target_link_libraries(dynamixel libdxl)


add_library(arduqbo_instructions_lib src/driver/arduqbo_instructions.cpp)
add_library(qboduino_driver_lib src/driver/qboduino_driver.cpp)
target_link_libraries(qboduino_driver_lib arduqbo_instructions_lib)
add_dependencies(qboduino_driver_lib qbo_arduqbo_generate_messages_cpp qbo_arduqbo_generate_services_cpp)

add_library(servos_lib src/servos.cpp)
target_link_libraries(servos_lib dynamixel libdxl)

add_library(base_controller_lib src/controllers/base_controller.cpp)
add_dependencies(base_controller_lib qbo_arduqbo_generate_messages_cpp qbo_arduqbo_generate_services_cpp)

add_library(battery_controller_lib src/controllers/battery_controller.cpp)
add_library(joint_controller_lib src/controllers/joint_controller.cpp)
target_link_libraries(joint_controller_lib servos_lib)

add_library(lcd_controller_lib src/controllers/lcd_controller.cpp)
add_library(mics_controller_lib src/controllers/mics_controller.cpp)
add_library(mouth_controller_lib src/controllers/mouth_controller.cpp)
add_library(nose_controller_lib src/controllers/nose_controller.cpp)
add_library(srf10_controller_lib src/controllers/srf10_controller.cpp)
add_dependencies(qboduino_driver_lib qbo_arduqbo_generate_messages_cpp qbo_arduqbo_generate_services_cpp)
add_library(irs_controller_lib src/controllers/infra_red_recievers_controller.cpp)
add_library(imu_controller_lib src/controllers/imu_controller.cpp)

## Declare a cpp executable

add_executable(qbo_arduqbo src/qbo_arduqbo.cpp)
add_dependencies(qbo_arduqbo qbo_arduqbo_generate_messages_cpp qbo_arduqbo_generate_services_cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes


target_link_libraries(qbo_arduqbo cereal_port qboduino_driver_lib base_controller_lib battery_controller_lib joint_controller_lib lcd_controller_lib mics_controller_lib mouth_controller_lib nose_controller_lib  imu_controller_lib  pthread dynamixel libdxl srf10_controller_lib irs_controller_lib  ${catkin_LIBRARIES})

#irs_controller_lib

## Declare a cpp library
# add_library(qbo_arduqbo
#   src/${PROJECT_NAME}/qbo_arduqbo.cpp
# )

# add_executable(qbo_arduqbo_node src/qbo_arduqbo_node.cpp)

## Add cmake target dependencies of the executable/library
## as an example, message headers may need to be generated before nodes
 #add_dependencies(qbo_arduqbo qbo_arduqbo_generate_messages_cpp)

## Specify libraries to link a library or executable target against
# target_link_libraries(qbo_arduqbo_node
#   ${catkin_LIBRARIES}
# )

#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
# install(PROGRAMS
#   scripts/my_python_script
#   DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark executables and/or libraries for installation
# install(TARGETS qbo_arduqbo qbo_arduqbo_node
#   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
#   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
# )

## Mark cpp header files for installation
# install(DIRECTORY include/${PROJECT_NAME}/
#   DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
#   FILES_MATCHING PATTERN "*.h"
#   PATTERN ".svn" EXCLUDE
# )

## Mark other files for installation (e.g. launch and bag files, etc.)
# install(FILES
#   # myfile1
#   # myfile2
#   DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
# )

#############
## Testing ##
#############

## Add gtest based cpp test target and link libraries
# catkin_add_gtest(${PROJECT_NAME}-test test/test_qbo_arduqbo.cpp)
# if(TARGET ${PROJECT_NAME}-test)
#   target_link_libraries(${PROJECT_NAME}-test ${PROJECT_NAME})
# endif()

## Add folders to be run by python nosetests
# catkin_add_nosetests(test)
