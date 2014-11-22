#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import math

from geometry_msgs.msg import Twist
from std_msgs.msg import String
from qbo_talk.srv import Text2Speach

        
def speak_this(text): # for qbo_talk
    global client_speak
    client_speak(str(text))

class neo_vocal_move:

    def __init__(self):
        global client_speak
        rospy.on_shutdown(self.cleanup)
        self.speed = 0.15
        self.msg = Twist()

        # publish to cmd_vel, subscribe to listen output
        self.pub_ = rospy.Publisher('cmd_vel', Twist, queue_size=10)
        rospy.Subscriber('listened', String, self.listen_callback)
        # call "/say" service to speak selected words
        client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)

        r = rospy.Rate(10.0)
        while not rospy.is_shutdown():
            self.pub_.publish(self.msg)
            r.sleep()

    def listen_callback(self, msg): # for qbo_listen
        print "Commande = ",msg.data


        if msg.data.find("plus_vite") > -1:
            speak_this("Ok, j'accélère")
            if self.speed <=0.15:
                self.msg.linear.x = self.msg.linear.x*2
                self.msg.angular.z = self.msg.angular.z*2
                self.speed = (self.speed+0.05)
        if msg.data.find("moins_vite") > -1:
            speak_this("Bien, je ralentis")
            if self.speed >=0.10:
                self.msg.linear.x = self.msg.linear.x/2
                self.msg.angular.z = self.msg.angular.z/2
                self.speed = (self.speed-0.05)


        if msg.data.find("avance") > -1 or msg.data.find("en_avant") > -1: 
            speak_this("Reçu, j'avance")   
            self.msg.linear.x = self.speed
            self.msg.angular.z = 0
        elif msg.data.find("tourne_a_gauche") > -1:
            speak_this("A gauche, bien")
            if self.msg.linear.x != 0:
                if self.msg.angular.z < self.speed:
                    self.msg.angular.z += 0.3
            else:        
                self.msg.angular.z = self.speed*2
        elif msg.data.find("tourne_a_droite") > -1: 
            speak_this("A droite, ok")   
            if self.msg.linear.x != 0:
                if self.msg.angular.z > -self.speed:
                    self.msg.angular.z -= 0.3
            else:        
                self.msg.angular.z = -self.speed*2
        elif msg.data.find("recule") > -1 or msg.data.find("en_arrière") > -1:
            speak_this("Je recule")
            self.msg.linear.x = -self.speed
            self.msg.angular.z = 0
        elif msg.data.find("stop") > -1 or msg.data.find("halte") > -1 or msg.data.find("arrêt") > -1 or msg.data.find("urgence") > -1 or msg.data.find("arrêt_d_urgence") > -1:   
            speak_this("Bien, je m'arrait")       
            self.msg = Twist()

        self.pub_.publish(self.msg)

    def cleanup(self):
        # stop QBO robot !
        twist = Twist()
        self.pub_.publish(twist)

if __name__=="__main__":
    rospy.init_node('neo_vocal_move')
    try:
        neo_vocal_move()
    except:
        pass

