#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
*************************************************************************
    A RETURN TO DOCK STATION WITH HELP OF AR-TAGS

    BIG THANKS TO PATRICK GOEBEL FOR TUTOS AND PY PROGRAMS
    SEE HIM ON : Pi Robot Project: http://www.pirobot.org

                         Vincent FOUCAULT       January 2016
*************************************************************************
'''

import os, sys
import rospy, subprocess
import smach
import smach_ros
import math
from math import copysign, cos, pi
from time import sleep
from ar_track_alvar_msgs.msg import AlvarMarkers
from std_msgs.msg import String
from sensor_msgs.msg import PointCloud
from geometry_msgs.msg import Twist, Point, PoseStamped
from qbo_talk.srv import Text2Speach


class Searching(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["aborted","GOOD"])

        # Set the shutdown function (stop the robot)
        rospy.on_shutdown(self.shutdown)
        # service for speech
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)    

        # How often should we update the robot's motion?
        self.rate = rospy.get_param("~rate", 5)
        self.r = rospy.Rate(self.rate)

        # The maximum rotation speed in radians per second
        self.max_angular_speed = rospy.get_param("~max_angular_speed", 0.1)
        # The minimum rotation speed in radians per second
        self.min_angular_speed = rospy.get_param("~min_angular_speed", 0.01)
        # The max linear speed in meters per second
        self.max_linear_speed = rospy.get_param("~max_linear_speed", 0.1)
        # The minimum linear speed in meters per second
        self.min_linear_speed = rospy.get_param("~min_linear_speed", 0.02)

        # The goal distance (in meters) to keep between the robot and the marker
        self.DockTagDistance_threshold = rospy.get_param("~DockTagDistance_threshold", 0.75)
        self.LeftTagDistance_threshold = rospy.get_param("~LeftTagDistance_threshold", 1.10)

        # How far away from the goal distance (in meters) before the robot reacts
        # dist threshold left_tag/xtion
        self.Left_x_threshold = rospy.get_param("~Left_x_threshold", 0.025) 
        # dist threshold dock_tag/xtion
        self.Dock_x_threshold = rospy.get_param("~Dock_x_threshold", 0.05)
        # final distance xtion/dock before turning 180°
        self.DockXFinal_threshold = rospy.get_param("~DockXFinal_threshold", 0.55) 
        # How far from center (in meters) before the robot reacts
        self.y_threshold = rospy.get_param("~y_threshold", 0.005) # 0.001

        # Publisher to control the robot's movement
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        # Intialize the movement command
        self.move_cmd = Twist()
        # Wait for the ar_pose_marker topic to become available
        rospy.loginfo("Waiting for ar_pose_marker topic...")
        rospy.wait_for_message('ar_pose_marker', AlvarMarkers)
        # Subscribe to the ar_pose_marker topic to get the image width and height
        rospy.Subscriber('ar_pose_marker', AlvarMarkers, self.set_cmd_vel)
        self.Left_tag_visible = False
        self.Dock_tag_visible = False
        self.Left_tag_dist_msg = 0
        self.Dock_tag_dist_msg = 0
        self.Left_tag_center_msg = 0
        self.Dock_tag_center_msg = 0

    def speak_this(self,text):
        self.client_speak(str(text))

    def set_cmd_vel(self, msg):

      try:
          for tag in msg.markers:
            if tag.id == 111 :
              self.Left_tag_visible = True
              self.Left_tag_dist_msg = tag.pose.pose.position.x
              self.Left_tag_center_msg = tag.pose.pose.position.y
            else :
              self.Left_tag_visible = False

            if tag.id == 222 :
              self.Dock_tag_visible = True
              self.Dock_tag_dist_msg = tag.pose.pose.position.x
              self.Dock_tag_center_msg = tag.pose.pose.position.y
            else :
              self.Dock_tag_visible = False
          
      except:
          return


    def execute(self, userdata):
 
      self.speak_this ("Bon, ou qu'il est mon lit ?")
      while not rospy.is_shutdown():

        while self.Left_tag_visible :
          #print "Left Tag Seen"
          # wile distance from left_tag to xtion isn't correct ...
          while abs(self.Left_tag_dist_msg - self.LeftTagDistance_threshold) > 0.05:
            speed = (self.Left_tag_dist_msg - self.LeftTagDistance_threshold)
            self.move_cmd.linear.x = copysign(max(self.min_linear_speed, min(self.max_linear_speed, abs(speed))), speed)
            speedR = self.Left_tag_center_msg 
            self.move_cmd.angular.z = copysign(self.min_angular_speed, speedR)
            if not self.Left_tag_visible :
              print "Left tag lost !!!"
              self.move_cmd.linear.x = 0.0
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()
          self.cmd_vel_pub.publish(Twist())
          rospy.sleep(0.1)
          while not self.Dock_tag_visible:
            self.move_cmd.linear.x = 0
            self.move_cmd.angular.z = - 0.25
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()
          print "	centering dock"
          while not abs(self.Dock_tag_center_msg) <= 0.01:
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = copysign(0.05, self.Dock_tag_center_msg)
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()
          self.cmd_vel_pub.publish(Twist())
          rospy.sleep(0.1)
          pass

        while self.Dock_tag_visible :
          #print "	Dock Tag Seen"
          # wile distance from dock_tag to xtion isn't correct ...
          while abs(self.Dock_tag_dist_msg - self.DockTagDistance_threshold) > 0.075:
            speed2 = (self.Dock_tag_dist_msg - self.DockTagDistance_threshold)
            self.move_cmd.linear.x = copysign(max(self.min_linear_speed, min(self.max_linear_speed, abs(speed2))), speed2)
            speedR2 = self.Dock_tag_center_msg 
            self.move_cmd.angular.z = copysign(self.min_angular_speed, speedR2)
            if not self.Dock_tag_visible :
              print "Dock tag lost !!!"
              self.move_cmd.linear.x = 0.0
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()
          self.cmd_vel_pub.publish(Twist())
          rospy.sleep(0.1)
          while not self.Left_tag_visible:
            self.move_cmd.linear.x = 0
            self.move_cmd.angular.z = 0.25
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()
          print "centering left_tag"
          while not abs(self.Left_tag_center_msg) <= 0.025:
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = copysign(0.05, self.Left_tag_center_msg)
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()
          self.cmd_vel_pub.publish(Twist())
          rospy.sleep(0.5)
          pass


        while abs(self.Left_tag_dist_msg - self.LeftTagDistance_threshold) <= self.Left_x_threshold and abs(self.Dock_tag_dist_msg - self.DockTagDistance_threshold) <= self.Dock_x_threshold:
          print "\n°°°°°°°°°°°°°°°°°°°°°°°"
          print "Approaching end phase !"
          while not self.Dock_tag_visible :
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = copysign(self.max_angular_speed, self.Dock_tag_center_msg)
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()
          print ">>> Looking for last distance..."
          self.speak_this ("J'y suis presque,") # speaks in french
          while not abs(self.Dock_tag_dist_msg - 0.50) <= self.Dock_x_threshold :
            speed = (self.Dock_tag_dist_msg - self.DockXFinal_threshold)
            self.move_cmd.linear.x = copysign(self.min_linear_speed, speed)
            self.move_cmd.angular.z = copysign(self.max_angular_speed, self.Dock_tag_center_msg)
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()
          print ">>> Last time centering..."
          print "°°°°°°°°°°°°°°°°°°°°°°°\n"
          while not abs(self.Dock_tag_center_msg) <= self.y_threshold:
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = copysign(0.015, self.Dock_tag_center_msg)
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()
          print ">>> I got it !!! Now, going to sleep !!!"
          rospy.sleep(0.5)
          return 'GOOD'

        # If no tag is seen !!!
        if not self.Left_tag_visible and not self.Dock_tag_visible :
            #print " Waiting for Tags"
            self.move_cmd.linear.x = 0.0
            self.move_cmd.angular.z = -self.max_angular_speed
            self.cmd_vel_pub.publish(self.move_cmd)
            self.r.sleep()


    def shutdown(self):
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel_pub.publish(Twist())
        rospy.sleep(1)


class GOOD(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["next_step"])

    def execute(self, userdata):
            print "Dock tag correctly centered on xtion cam picture"
            rospy.sleep(1)
            return 'next_step'


class Turning(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["next_step"])
        self.rate = rospy.get_param("~rate", 10)
        self.r = rospy.Rate(self.rate)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        self.move_cmd = Twist()

    def execute(self, userdata):
            print " turning 180°"
            self.move_cmd.angular.z = 0.454 # 0.485 # Normally it should be same value than "speed" (Angular : 0.45 m/s), but minor mod is necessary to correct robot moves precision !
            self.move_cmd.linear.x = 0
            goal_angle = pi
            speed = goal_angle/0.45
            rDuration = int(speed*self.rate)
            for t in range(rDuration) :
              self.cmd_vel_pub.publish(self.move_cmd)
              self.r.sleep()
            rospy.sleep(1)
            return 'next_step'


class Moving_backward(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["next_step"])
        self.rate = rospy.get_param("~rate", 10)
        self.r = rospy.Rate(self.rate)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        self.move_cmd = Twist()
        client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)

    def execute(self, userdata):
            print " Moving backward, until Docking"
            val = (-0.90)
            self.lD = int(val/-0.15)
            self.lDuration = int(self.lD*self.rate)
            self.move_cmd.angular.z = 0
            self.move_cmd.linear.x = -0.18
            for t in range(self.lDuration) :
              self.cmd_vel_pub.publish(self.move_cmd)
              self.r.sleep()
            rospy.sleep(1)
            return 'next_step'



class Finished(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["exit"])
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=5)
        self.move_cmd = Twist()
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)

    def run_process(self,command = ""):
        if command != "":
            return subprocess.Popen(command.split())
        else:
            return -1

    def speak_this(self,text):
        self.client_speak(str(text))
    
    def execute(self, userdata):
        rospy.sleep(5)
        self.speak_this ("Voilà. Fini. Bonne nuit les gars,")  # speaks in french
        print " I'm charging, I think !"
        rospy.loginfo("Stopping the robot...")
        self.cmd_vel_pub.publish(Twist())
        self.run_process("rosnode kill /ar_track_alvar")
        return 'exit'
        rospy.signal_shutdown(Finished)
        sys.exit()



def main():
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['exit'])
    with sm:
        smach.StateMachine.add('SEARCHING', Searching(), transitions={'aborted':'SEARCHING','GOOD':'GOOD'})
        smach.StateMachine.add('GOOD', GOOD(), transitions={'next_step':'TURNING'})
        smach.StateMachine.add('TURNING', Turning(), transitions={'next_step':'BACKWARD'})
        smach.StateMachine.add('BACKWARD', Moving_backward(), transitions={'next_step':'FINISHED'})
        smach.StateMachine.add('FINISHED', Finished())
    sis= smach_ros.IntrospectionServer('server_name',sm,'/Return_To_Dockstation')
    sis.start()

    # Execute SMACH plan
    rospy.sleep(2)
    rospy.loginfo("RTH launched")
    outcome = sm.execute()
    rospy.loginfo('RTH Finished')
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    try:
        rospy.init_node("ar_RTH")
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo("RTH node terminated.")
