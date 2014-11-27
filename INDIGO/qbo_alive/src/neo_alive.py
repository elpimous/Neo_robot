#!/usr/bin/env python
# -*- coding: utf-8 -*-


#********************************************************************
#
#
#                        Qbo is alive !!!
#
#              - curious, Néo moves head and speak
#
#               - it uses mouth, eyelids and nose 
#
#                      elpimous12@orange.fr
#
#           ps : good tutorial to know publishing orders
#********************************************************************

import rospy
import random
from random import choice, uniform
import time
from time import sleep

from qbo_talk.srv import Text2Speach # voice
from geometry_msgs.msg import Twist # body moves
from sensor_msgs.msg import JointState # head moves
from std_msgs.msg import UInt8 # nose colors

def speak_this(text):
 global client_speak
 client_speak(text)

def main():
  global client_speak
  baseMovePub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
  headPub = rospy.Publisher("/cmd_joints", JointState, queue_size=1)
  nosePub = rospy.Publisher("/cmd_nose", UInt8, queue_size=1)
  eyelidsPub = rospy.Publisher("/cmd_", UInt8, queue_size=1)

  while not rospy.is_shutdown(): # start loop

    localHour = int(time.strftime('%H',time.localtime())) # real local time
    while localHour < 22 and localHour >= 9: # qbo alive between 9am and 10pm

###  Base Move  ###
      bodyMove = Twist()
      bodyMove.linear.x = random.uniform(-0.12,0.12)
      bodyMove.angular.z = random.uniform(-0.3,0.3)
      #TODO odom use to limit position and angular final max rotations (let qbo randomly move in a circle of diameter 1.5 m)
      baseMovePub.publish(bodyMove)


###  head moves  ###
      panTilt = JointState()
      panTilt.name=['head_tilt_joint', 'head_pan_joint'] # L/R, U/D

      tiltPos = random.uniform(0,-1)
      panPos = random.uniform(1,-1)

      panTilt.position=[tiltPos, panPos] # tilt & pan position
      #panTiltTemp.temperature=[tiltTemp,panTemp]
      tiltVel = random.uniform(0.1,1)
      panVel = random.uniform(0.1,1)
      panTilt.velocity=[tiltVel, panVel] # tilt & pan speed

      # TODO
      #if tiltTemp > 50 or panTemp > 50 : # dynamixels too hot !!! maximum limit is 70°c
       # rospy.loginfo("Dynamixels too hot ! Security pause started")
       # sleep(600)# pause 10 minutes, waiting for cold dynamixels


      headPub.publish(panTilt)


###  Nose colors  ###
      noseColor = UInt8() # publish nose number for color changing
      for i in range(0,10): # cycle colors for 2 sec 
         noseColor = random.uniform(0,3)
         nosePub.publish(noseColor)
         i+=1 
         rospy.sleep(0.2) # loops nose color 10 times a second


###  Eyelids  ###
      eyeslids = UInt8() 



###  Voice  ###
      client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
      sentences = ["Bon, j'ai un peu la dalle, Ya quoi à manger,","Ah, oui, quand-même, C'est pas faux.","j'ai besoin de me recharger, je pense","Maintenant que je dispose d'une intelligence artificielle, je me pose plein de questions","Si seulement je pouvais penser par moimême,","Je ferai bien un truc,là, du genre, parler pour ne rien dire, juste comme ça","Je me pose plein de questions, trop, peut_être","yaisse, je suis au top, ou du moins je le pense","Euh, je pensais à un truc,super compliqué,","En fait, qui suis-je? Un vrai robot,","Je suis bardé de capteurs, Je suis prêt","Oh, le temps ma l'air bien humide","Mais bien sur,","Un truc de ouf, Et si je cartographiai le salon,","Dis moi qui tu es, Je te dirai qui tu es.","On est comme on est, Et on est, ou pas.","Je suis vert, c'est un fait, Mais j'aurais bien aimé être tout blanc","Tout ce pouvoir dans un aussi petit corps, Je vais exploser","Et toi, t'en penses quoi de ma présence,","J'ai envie de foncer plein gaz dans la maison","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","","",""]
      speak_this(choice(sentences))
      rospy.loginfo("end of actual life loop")
      rospy.sleep(random.uniform (5,10)) # time waiting for next loop


    rospy.loginfo("Sleeping")

#Main instuctions
if __name__ == '__main__':
   try:
      rospy.init_node('neo_alive_node', anonymous=True)
      main()
   except rospy.ROSInterruptException:
      print "interrupted  !"
