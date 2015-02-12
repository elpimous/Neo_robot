#!/usr/bin/env python
# -*- coding: utf-8 -*-


######################################################################################################
#                                                                                                    #
# A SIMPLE NODE TO LET ROBOT SPEAK AND TELL US IF : CHARGE IS NEEDED / FULL CHARGE / FULL DISCHARGE  #
#                                                                                                    #
#   use of .wav files with sox to let robot speak... Waiting for SAPI5 linux perfect integrity       #
#                                                                                                    #
#              Vincent FOUCAULT       elpimous12@orange.fr            FEV. 2015                      #
######################################################################################################


import rospy
import random
import os
from random import choice
from time import sleep
from qbo_arduqbo.msg import BatteryLevel


def run_process(command = ""):
    if command != "":
        return os.system(command)
    else:
        return -1

# hello, startup message
hello = ("hello1","hello2","hello3","hello4")
run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/"+(random.choice(hello))+".wav")

class energy:

  def __init__(self):
#initialize node
    rospy.init_node('qbo_energy')

    self.voltage = 0.
    self.voltMini = "11.5" # you can change mini
    self.stat = 0.
    rospy.Subscriber('/battery_state', BatteryLevel, self.batteryInfo)
    self.wavCh_needed = False


# Decimal .. Binary ........................Description..................................................................
# 13 --------- 001101 -- 001- Battery charging at constant current / 1-External Power present / 0-PC off / 1-Q.boards on.
# 15 --------- 001111 -- 001- Battery charging at constant current / 1-External Power present / 1-PC on / 1-Q.boards on.
# 21 --------- 010101 -- 010- Battery charging at constant voltage / 1-External Power present / 0-PC off / 1-Q.boards on.
# 29 --------- 011101 -- 011- Battery fully charged / 1-External Power present / 0-PC off / 1-Q.boards on.
# 31 --------- 011111 -- 011- Battery fully charged / 1-External Power present / 1-PC on / 1-Q.boards on.
# 35 --------- 100011 -- 100- Battery discharging / 0-Not External Power / 1-PC on / 1-Q.boards on.


  def batteryInfo(self, data):
      self.voltage = str(data.level)
      self.stat = str(data.stat)
      #print "capacité batterie : "+self.voltage+" et état actuel : "+self.stat


      # if battery voltage too low (see L.24) and not plugged in    
      if self.stat == "35" and self.voltage < self.voltMini : # attention shutdown soon...
        rospy.loginfo("Attention, batteries presque vides !")
        run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/attention_recharge.wav")
        sleep(60) # continue alert eack 60 seconds, until qbo is plugged in
        
        
      # if battery fully charged and plugged in  (nearly 13.5v plugged and 13.1v unplugged)
      if self.voltage >= "13.5" : # fully charged
        rospy.loginfo("Batteries chargées !")
        run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/batteries_chargees.wav")
        sleep(600) # 10 minutes    


      # when you plug power on qbo side, you'll hear : charging !!			
      if self.stat == "15" and self.wavCh_needed == True : # charging and no already spoken
        rospy.loginfo("Batteries en charge !")
        run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/recharge.wav")
        self.wavCh_needed = False # speak just one time
      if self.stat == "35" :
        self.wavCh_needed = True # can speak again one time if plugged in


# when plugged in, if Voltage doesn't grows, 2 possibilities : charger broken, or unconnected			
# if AC/DC wall is without power, and plugged in qbo,
# qbo will stay in state 35 (discharging, until low power alert)
        
        
if __name__ == '__main__':
	
  try:
    node = energy()
    rospy.spin()
    
  except rospy.ROSInterruptException:
    print "end of qbo_energy node"
    
    
