#!/usr/bin/env python
# -*- coding: utf-8 -*-


######################################################################################################
#                                                                                                    #
# A SIMPLE NODE TO LET ROBOT SPEAK AND TELL US IF : CHARGE IS NEEDED / FULL CHARGE / FULL DISCHARGE  #
#                                                   / ALERTS ON SOME VOLTAGES                        #
#                                                                                                    #
#              Vincent FOUCAULT       elpimous12@orange.fr            FEV. 2015                      #
######################################################################################################


import rospy
import random
import os
from lib_qbo_pyarduqbo import qbo_control_client
from random import choice
from time import sleep
from std_msgs.msg import String, Float32, Int8
from qbo_talk.srv import Text2Speach
from qbo_arduqbo.msg import BatteryLevel

"""
def run_process(command = ""):
    if command != "":
        return os.system(command)
    else:
        return -1
"""


def speak_this(text):
    client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
    client_speak(str(text))

# hello, startup message / usefull when launch at startup
hello = ("Bonjour, je suis prait à apprendre","Salut, On fait-quoi, aujourd'hui ?","Super, encore-une-bonne journée qui commence,","c'est parti")
speak_this(random.choice(hello))

class energy:

  def __init__(self):
#initialize node
    rospy.init_node('qbo_energy')
    self.voltage = float(0.0)
    self.voltMini = float(11.8) # you can change mini   # 11.8
    self.voltMaxi = float(13.39)  # for my hybrid lifepo pack
    rospy.Subscriber('/battery_state', BatteryLevel, self.volts)
    self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
    self.pub = rospy.Publisher('/chargeNeeded', String, queue_size=10)
    self.wavCh_needed = False
    self.wavDeb = True
    self.thirteenVolts = True
    self.twelvepointfiveVolts = True
    self.twelveVolts = True
    self.blabla = False

# Decimal .. Binary ........................Description..................................................................
# 13 --------- 001101 -- 001- Battery charging at constant current / 1-External Power present / 0-PC off / 1-Q.boards on.
# 15 --------- 001111 -- 001- Battery charging at constant current / 1-External Power present / 1-PC on / 1-Q.boards on.
# 21 --------- 010101 -- 010- Battery charging at constant voltage / 1-External Power present / 0-PC off / 1-Q.boards on.
# 29 --------- 011101 -- 011- Battery fully charged / 1-External Power present / 0-PC off / 1-Q.boards on.
# 31 --------- 011111 -- 011- Battery fully charged / 1-External Power present / 1-PC on / 1-Q.boards on.
# 35 --------- 100011 -- 100- Battery discharging / 0-Not External Power / 1-PC on / 1-Q.boards on.


  def speak_this(self,text): # robot voice
    self.client_speak(str(text))

  def volts(self, data):  # different alerts with different voltage values 
      self.voltage = (data.level)
      if self.voltage >= self.voltMaxi and self.blabla == False: # fully charged
        self.speak_this("Mes batteries sont totalement chargées")
        self.blabla = True
      if self.voltage == float(13.00) and self.thirteenVolts == True:
        self.speak_this("ma tension interne, indique 13 volts")
        self.thirteenVolts = False
        self.twelvepointfiveVolts == True
        self.twelveVolts == True
        self.blabla = False
      if self.voltage == float(12.50) and self.twelvepointfiveVolts == True:
        rospy.loginfo("batt 12.5V !")
        self.speak_this("ma tension interne, indique 12 volte cinq")
        self.twelvepointfiveVolts = False
        self.thirteenVolts == True
        self.twelveVolts == True 
        self.blabla = False       
      if self.voltage == float(12.00) and self.twelveVolts == True:
        self.speak_this("ma tension interne, indique 12 volts")
        self.twelveVolts = False
        self.thirteenVolts == True
        self.twelvepointfiveVolts == True
        self.blabla = False
      #print "volt : "+str(self.voltage)

      self.stat = (data.stat) 

      if self.stat == int(35) and self.voltage < self.voltMini  and self.blabla == False: # attention shutdown soon...
        self.speak_this("Attention, attention. Mes batteries sont presque vides. je dois retourner sur ma base.")
        self.blabla = True

      if self.stat == int(15) and self.wavCh_needed == True : # charging and no already spoken
        self.speak_this("mes batteries sont tant charge")
        self.wavCh_needed = False # speak just one time
        self.wavDeb = True # can speak when plug in power
        self.pub.publish('charging')
      if self.stat == int(35) :  # if unplugged, robot uses it internal battery  
        self.wavCh_needed = True # can speak again one time if plugged in
        if self.wavDeb == True:
          self.speak_this("je bascule sur mes batteries zinterne")
          self.wavDeb = False    
      #print "                                      stat : " + str(self.stat) 

# when plugged in, if Voltage doesn't grows, 2 possibilities : charger broken, or unconnected			
# if AC/DC wall is without power, and plugged in qbo,
# qbo will stay in state 35 (discharging, until low power alert)


if __name__ == '__main__':

  try:
    node = energy()
    rospy.spin()

  except rospy.ROSInterruptException:
    print "end of qbo_energy node"
    
    
