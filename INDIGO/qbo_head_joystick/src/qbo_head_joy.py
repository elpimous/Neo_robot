#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# A python program by Vincent FOUCAULT
# a program who uses head movments as joystick inputs
# commands are "UP / DOWN / LEFT / RIGHT"
#
#########################################################


import rospy, roslib
from time import sleep
from std_msgs.msg import String
from sensor_msgs.msg import JointState

class headMoveJoy():

    def __init__(self):
        
        # init ros node
        rospy.init_node('qbo_head_joy')
        # publisher
        self.headJoyPub = rospy.Publisher('/head_joy', String, queue_size=1)
        # subscriber
	self.headSub = rospy.Subscriber('/joint_states', JointState, self.data_head_pose)
        # loop pause
        self.rate = rospy.get_param("~rate", 3)
        self.r = rospy.Rate(self.rate)


    # receive head Dynamixels informations and put specific ones in variables
    def data_head_pose(self, data): 
        self.originHP = data.position[2]
        self.originHT = data.position[3]

    # create neutral movements limits
    def values(self):
        rospy.wait_for_message("joint_states", JointState)
        self.up = self.originHT+0.1
	self.down = self.originHT-0.2
	self.left = self.originHP+0.1
	self.right = self.originHP-0.1


    def main(self):

        self.values()

        # make loop
        while not rospy.is_shutdown():
 
            # create over limit head movements
            if float(self.originHT) > float(self.up) :
                # send appropriate command
                self.headJoyPub.publish("down")
            if float(self.originHT) < float(self.down) :
                self.headJoyPub.publish("up")
            if float(self.originHP) > float(self.left) :
                self.headJoyPub.publish("right")
            if float(self.originHP) < float(self.right) :
                self.headJoyPub.publish("left")
            self.r.sleep()
            


if __name__ == "__main__":
    try:
       start = headMoveJoy()
       start.main()
    except rospy.ROSInterruptException: 
       rospy.loginfo ("exiting head_joy node !")
    pass
