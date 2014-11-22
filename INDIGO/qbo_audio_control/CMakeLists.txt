cmake_minimum_required(VERSION 2.8.3)
project(qbo_audio_control)

find_package(catkin REQUIRED COMPONENTS
  roscpp
)

catkin_package(

)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

add_executable(qbo_audio_control src/audio_control.cpp)

target_link_libraries(${PROJECT_NAME} pulse)
target_link_libraries(${PROJECT_NAME} stdc++)
target_link_libraries(${PROJECT_NAME} ${catkin_LIBRARIES})
