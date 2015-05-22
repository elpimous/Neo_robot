#!/usr/bin/env python
# coding: utf-8
"""
A ROS-HYDRO/INDIGO CATKIN FACE RECOGNITION PROGRAM :
HEAD PAUSED IN SPECIFIC UP POSITION
WHEN SEEN FACE, START TRACKING FACE, AND RECOGNIZE PERSON
WHEN IMPOSSIBLE TO TRACK FOR 1 MINUTE, RETURN TO UP POSITION AND PAUSE
THANKS TO ROS::SMACH
"""

import rospy
import smach # smach ready for use
import subprocess
from actionlib import *
from actionlib.msg import *
from qbo_arduqbo.msg import Nose # for nose color modif.
from std_msgs.msg import String
from qbo_face_msgs.msg import FacePosAndDist # for green tracking box localization in picture
from face_recognition.msg import FaceRecognitionAction, FaceRecognitionGoal, FaceRecognitionResult # for actionlib


class face_reco:
  
  def __init__(self):
    rospy.init_node('qbo_face_analysis')
    # topic to recover "face_detected", "distance_to_head" informations
    # try on terminal : rostopic echo /qbo_face_tracking/face_pos_and_dist , to see RT values
    rospy.Subscriber("/qbo_face_tracking/face_pos_and_dist", FacePosAndDist, self.face_pos_callback)
    # publishing recognition result in "recognized" topic
    self.pubFace = rospy.Publisher('face_recognition/recognized', String, queue_size=1)
    # Goal state return values
    self.goal_states = ['RECALLING', 'REJECTED', 'ABORTED', 'SUCCEEDED']
    self.nose_pub = rospy.Publisher('/cmd_nose',Nose , queue_size=1)
    self.nose = Nose()
    self.nose.color=0
    self.face_stabilizer = 0
    self.stabilizer_max = 20
    self.distance_head_max = 2
    self.face_detected = False
    self.recognizedName = ""
    self.ready_for_recognition = False
    #Topic for Actionlib server Recognition
    self.recognition = actionlib.SimpleActionClient("face_recognition", FaceRecognitionAction)


  def face_pos_callback(self,data):

    #print str(data.face_detected)+" *** "+str(data.distance_to_head)
    self.face_detected = data.face_detected
    self.distance_face = data.distance_to_head
    #rospy.loginfo ("la stabilisation est de : "+str(self.face_stabilizer)+"/"+str(self.stabilizer_max))
    self.nose.color= 0
    self.nose_pub.publish (self.nose)

    # wait for tracking stabilization
    if data.face_detected and data.distance_to_head<self.distance_head_max and self.face_stabilizer < self.stabilizer_max:
       self.face_stabilizer+=1 # face ok --- up
       self.nose.color=3
       self.nose_pub.publish (self.nose)
       self.ready_for_recognition = False

    elif not data.face_detected and self.face_stabilizer > 0:
       self.face_stabilizer -= 4 # no face --- down
       self.nose.color=1
       self.nose_pub.publish (self.nose)
       self.ready_for_recognition = False

    if self.face_stabilizer <= 0: # limit stabilizer to a minimum of 0
       self.face_stabilizer = 0
       self.nose.color=0
       self.nose_pub.publish (self.nose)
       self.ready_for_recognition = False

    if self.face_stabilizer >= self.stabilizer_max: # limit stabilizer to a maximum of max
       #print " stabilisé, pret !!!"
       self.face_stabilizer = self.stabilizer_max
       self.nose.color=2
       self.nose_pub.publish (self.nose)
       self.ready_for_recognition = True
    
    if 0 < self.face_stabilizer < self.stabilizer_max :
       self.notSure = str("unknown")
       self.pubFace.publish(self.notSure)
    

  # if face is well stabilized, recognition starts
  def start_recognition(self):
      while not rospy.is_shutdown():
        if self.ready_for_recognition == True:
          # send orders to  face recognition server  
          self.recognitionGoal = FaceRecognitionGoal()
          self.recognitionGoal.order_id = 0
          self.recognitionGoal.order_argument="none"
          self.recognition.send_goal(self.recognitionGoal)
          self.recognition.wait_for_result()
          #get result from face recognition server
          result = self.recognition.get_result()
          name = result.names
          #confidence = result.confidence
          self.recognizedName = str(name).replace("['","").replace("']","")
          #self.recognizedConfidence = str(confidence)
          self.pubFace.publish(self.recognizedName)
          state = self.recognition.get_state()
          print "voici l'etat:"+ str(self.goal_states[state])+" et le nom: "+self.recognizedName
          
        else:
          continue

a=face_reco()
a.start_recognition()

if __name__ == '__main__':
  try:
    rospy.spin()
  except rospy.ROSInterruptException:
    print "interrupted  !" 
