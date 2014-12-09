#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import random
from sensor_msgs.msg import PointCloud,Imu
from geometry_msgs.msg import Twist
from time import sleep

class randomMoveObstacleDetector:

  def __init__(self):
#initialize node
    rospy.init_node('qbo_random_move_avoid_obstacles')

    self.angularCoeff = .09 # with this value, angular speed changes with distance, test with slow changes / 0.11
    self.linearCoeff = 0.12 # idem, but with linear speed / 0.13
    self.random = random.uniform(-0.04,0.04)
    self.wallDetectionDistance = 0.6 # limitation to 180cm max (maxi 2m, so small security)

    self.frontLeftDistance = 0. # Front SRF10 sensors
    self.frontRightDistance = 0. 


    self.floorWallDistance = 0. # Floor sensor value
    self.floorDistanceOk = True
    self.floorDistance = 0.24
    self.floorInterval = 0.08 # slightly modify, depending of your floor material (mine : lay)

    self.wallDistanceOk = True
    self.wallInterval = 0.04 # slightly modify, depending of your wall material

    self.imuAngleOk = True
    self.imuMaxAngle = -5 # slightly modify if carpets, small walls...

    # useful to let robot know where it went from, and best direction to use.
    self.last_turn_direction=True # means last turn to right

    #create subscribers to srf and floor sensors
    rospy.Subscriber('/distance_sensors_state/front_left_srf10', PointCloud, self.frontLeftSensorCallback)
    rospy.Subscriber('/distance_sensors_state/front_right_srf10', PointCloud, self.frontRightSensorCallback)

    rospy.Subscriber('/distance_sensors_state/floor_sensor', PointCloud, self.floorSensorCallback)

    rospy.Subscriber('/imu_state/data', Imu, self.imuSensorCallback)

    rospy.Subscriber('/qbo_random_move/obstacle_avoidance_twist', Twist, self.twistCallback)# recover topic from qbo_explore

    self.twistPublisher = rospy.Publisher("/output_twist", Twist, queue_size=1)


  def frontLeftSensorCallback(self, data):
    self.frontLeftDistance = data.points[0].x
    if self.frontLeftDistance ==0:
      self.frontLeftDistance = 3

  def frontRightSensorCallback(self, data):
    self.frontRightDistance = data.points[0].x
    if self.frontRightDistance ==0:
      self.frontRightDistance = 3

  def floorSensorCallback(self, data):
    self.floorWallDistance = data.points[0].x
    self.floorDistanceOk = (self.floorWallDistance <= (self.floorDistance + self.floorInterval))# 0.32
    if not self.floorDistanceOk:
      print "plus de sol !!"
    self.wallDistanceOk = (self.floorWallDistance >= 0.16)#
    if not self.wallDistanceOk:
      print "                  obstacle frontal détecté !!"

  def imuSensorCallback(self, data):
    self.imuAngleOk = (data.linear_acceleration.x > self.imuMaxAngle)
    if not self.imuAngleOk :
      print "risque de chute arrière !!"


  def twistCallback(self, data): # TODO calculate angles for better move. Ex : left_srf/floor, left_srf/right_srf, right_srf/floor
                                 # Ex : if left_srf == 2(right_srt), turn 90° left...

#****************** AVOIDING BACK-FALLING *****************************

    while not self.floorDistanceOk or not self.wallDistanceOk or not self.imuAngleOk :
      # si apres un virage droite, detection vide ou chute arrière, recul et tourne vers droite, pour finir le virage
      # if after a right turn, robot detects an immediat obstacle, or a fall risk, robot goes backward and turn right
      if self.last_turn_direction==True:
          data.linear.x = -0.2
          data.angular.z = random.uniform(-0.3,-0.6)
          self.last_turn_direction=True
          sleep(1)
      elif self.last_turn_direction==False:
          data.linear.x = -0.2
          data.angular.z = random.uniform(0.3,0.6)
          self.last_turn_direction=False
          sleep(1)
      sleep(0.1)
    else:

#****************** NO OBSTACLES / FULL SPEED  ************************OK

      if self.frontRightDistance > 1.5 and self.frontLeftDistance > 1.5:
        data.linear.x = 0.15
        data.angular.z

#********************* RIGHT OBSTACLE ONLY ****************************OK

      elif self.frontRightDistance <  self.frontLeftDistance: # (chair leg ?)
        #print "                             obstacle DROIT détecté !!"
        if self.frontRightDistance <= 0.5: # obstacle à moins de 20 cm du capteur
          data.linear.x = -0.2
          data.angular.z = self.random + (self.angularCoeff/self.frontRightDistance)# ******** faire de meme avec le linear !!!
          sleep(1)
        data.linear.x = (self.linearCoeff*self.frontRightDistance)
        data.angular.z = self.random + (self.angularCoeff/self.frontRightDistance)
        self.last_turn_direction=True

#********************** LEFT OBSTACLE ONLY ****************************OK

      elif self.frontRightDistance > self.frontLeftDistance: # (chair leg ?)
        #print " obstacle GAUCHE détecté !!"
        if self.frontLeftDistance <= 0.5:
          data.linear.x = -0.2
          data.angular.z = -(self.random + (self.angularCoeff/self.frontLeftDistance))
          sleep(1)
        data.linear.x = (self.linearCoeff*self.frontLeftDistance)
        data.angular.z = -(self.random + (self.angularCoeff/self.frontLeftDistance))
        self.last_turn_direction=True



    self.twistPublisher.publish(data)  


#/tf
#transform: 
#      translation: 
 #       x: 7.34073114395  utiliser variation sur 0.01

#/odom
#twist: 
#  twist: 
#    linear: 
#     x: 0.0


if __name__ == '__main__':
  try:
    node = randomMoveObstacleDetector()
    rospy.spin()
  except rospy.ROSInterruptException:
    print "interrupted  !"
