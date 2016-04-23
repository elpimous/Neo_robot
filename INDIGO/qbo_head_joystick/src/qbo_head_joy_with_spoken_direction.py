#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, roslib
from time import sleep
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from qbo_talk.srv import Text2Speach

class headMoveJoy():

    def __init__(self):
        
        rospy.init_node('qbo_head_joy')
        # publisher
        self.headJoyPub = rospy.Publisher('/head_joy', String, queue_size=1)
        # subscriber
	self.headSub = rospy.Subscriber('/joint_states', JointState, self.data_head_pose)
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
        # loop pause
        self.rate = rospy.get_param("~rate", 3)
        self.r = rospy.Rate(self.rate)
        self.rate2 = rospy.get_param("~rate", 1)
        self.r2 = rospy.Rate(self.rate2)


    def speak_this(self,text): # robot voice
        self.client_speak(str(text))


    def data_head_pose(self, data): 
        self.originHP = data.position[2]
        self.originHT = data.position[3]
        #print "ok"
        #self.r.sleep()

    def values(self):
        rospy.wait_for_message("joint_states", JointState)
        self.up = self.originHT+0.1
	self.down = self.originHT-0.2
	self.left = self.originHP+0.1
	self.right = self.originHP-0.1
        #self.r2.sleep()

    def main(self):
        self.speak_this("mouvements de tête OK")
        self.values()
        while not rospy.is_shutdown():
            if float(self.originHT) > float(self.up) :
            	self.speak_this("bas")
                self.headJoyPub.publish("down")
            if float(self.originHT) < float(self.down) :
            	self.speak_this("haut")
                self.headJoyPub.publish("up")
            if float(self.originHP) > float(self.left) :
            	self.speak_this("droite")
                self.headJoyPub.publish("right")
            if float(self.originHP) < float(self.right) :
            	self.speak_this("gauche")
                self.headJoyPub.publish("left")
            self.r.sleep()
            


if __name__ == "__main__":
    try:
       start = headMoveJoy()
       start.main()
       #rospy.spin()
    except rospy.ROSInterruptException: 
       rospy.loginfo ("exiting head_joy node !")
    pass
