#!/usr/bin/env python
# coding: utf-8

#=================================
# a simple face recognition test
# When qbo detects a person
# it says his name
#=================================

import rospy
import roscpp
import subprocess
from time import sleep
from qbo_talk.srv import Text2Speach
from std_msgs.msg import String
from face_recognition import FaceRecognitionActionFeedback
rospy.Subscriber('/face_recognition/feedback', FaceRecognitionActionFeedback, faceName)

def speak_this(text):
  global client_speak
  client_speak(str(text))
 
def run_process(command = ""):
    if command != "":
        return subprocess.Popen(command.split())
    else:
        return -1
  
def faceName(data):
  recoName = data.feedback.names.replace("['","").replace("']","") 
  print recoName
  
  
def faceRecoStartup(): # qbo_camera node must work first
      client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach) # voice

  
if __name__ == '__main__':
    try:
        faceRecoStartup()
        rospy.spin()
    except rospy.ROSInterruptException:pass

