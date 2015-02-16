#!/usr/bin/env python
# -*- coding: utf-8 -*-


######################################################################################################
#                                                                                                    #
# A SIMPLE NODE TO LET ROBOT SPEAK AND TELL US IF : CHARGE IS NEEDED / FULL CHARGE / FULL DISCHARGE  #
#                                                   / ALERTS ON SOME VOLTAGES                        #
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

# hello, startup message / usefull when launch at startup
hello = ("hello1","hello2","hello3","hello4")
run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/"+(random.choice(hello))+".wav")



class energy:

  def __init__(self):
#initialize node
    rospy.init_node('qbo_energy')
    self.voltage = 0.
    self.voltMini = 11.7 # you can change mini 
    self.voltMaxi = 13.39  # for my hybrid lifepo pack
    self.stat = 0.
    rospy.Subscriber('/battery_state', BatteryLevel, self.fullyCharged)
    rospy.Subscriber('/battery_state', BatteryLevel, self.empty)
    rospy.Subscriber('/battery_state', BatteryLevel, self.plug)
    rospy.Subscriber('/battery_state', BatteryLevel, self.volts)    
    self.wavCh_needed = False
    self.wavDeb = True
    self.thirteenVolts = True
    self.twelvepointfiveVolts = True
    self.twelveVolts = True


# Decimal .. Binary ........................Description..................................................................
# 13 --------- 001101 -- 001- Battery charging at constant current / 1-External Power present / 0-PC off / 1-Q.boards on.
# 15 --------- 001111 -- 001- Battery charging at constant current / 1-External Power present / 1-PC on / 1-Q.boards on.
# 21 --------- 010101 -- 010- Battery charging at constant voltage / 1-External Power present / 0-PC off / 1-Q.boards on.
# 29 --------- 011101 -- 011- Battery fully charged / 1-External Power present / 0-PC off / 1-Q.boards on.
# 31 --------- 011111 -- 011- Battery fully charged / 1-External Power present / 1-PC on / 1-Q.boards on.
# 35 --------- 100011 -- 100- Battery discharging / 0-Not External Power / 1-PC on / 1-Q.boards on.


  def fullyCharged(self, data):  # if battery fully charged and plugged in  (nearly 13.9v plugged and 13.1v unplugged)
      self.voltage = (data.level)
      self.stat = str(data.stat)
      if self.voltage >= self.voltMaxi : # fully charged
        rospy.loginfo("Batteries chargées !")
        run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/batteries_chargees.wav")
        print"tout est chargé"
      else :
        pass

  def empty(self, data):  # if battery voltage too low and not plugged in  
      self.voltage = (data.level)
      self.stat = str(data.stat)    
      if self.stat == "35" and self.voltage < self.voltMini : # attention shutdown soon...
        rospy.loginfo("Attention, batteries presque vides !")
        run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/attention_recharge.wav")


  def plug(self, data):  # when you plug power on qbo side, you'll hear : charging !!
      self.stat = str(data.stat)               
      if self.stat == "15" and self.wavCh_needed == True : # charging and no already spoken
        rospy.loginfo("Batteries en charge !")
        run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/recharge.wav")
        self.wavCh_needed = False # speak just one time
        self.wavDeb = True # can speak when plug in power
      if self.stat == "35" :  # if unplugged, robot uses it internal battery  
        self.wavCh_needed = True # can speak again one time if plugged in
        if self.wavDeb == True:
          rospy.loginfo("Robot débranché !")
          run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/unplugged.wav")
          self.wavDeb = False    


  def volts(self, data):  # different alerts with different voltage values  
      self.voltage = (data.level)
      if self.voltage == 13.00 and self.thirteenVolts == True:
        run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/13.wav")
        self.thirteenVolts = False
        self.twelvepointfiveVolts == True
        self.twelveVolts == True
      if self.voltage == 12.50 and self.twelvepointfiveVolts == True:
        rospy.loginfo("batt 12.5V !")
        run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/12_5.wav")
        self.twelvepointfiveVolts = False
        self.thirteenVolts == True
        self.twelveVolts == True        
      if self.voltage == 12.00 and self.twelveVolts == True:
        run_process("play /opt/ros/hydro/stacks/qbo_energy/wav-files/12.wav")
        self.twelveVolts = False
        self.thirteenVolts == True
        self.twelvepointfiveVolts == True


# when plugged in, if Voltage doesn't grows, 2 possibilities : charger broken, or unconnected			
# if AC/DC wall is without power, and plugged in qbo,
# qbo will stay in state 35 (discharging, until low power alert)


if __name__ == '__main__':

  try:
    node = energy()
    rospy.spin()

  except rospy.ROSInterruptException:
    print "end of qbo_energy node"
    
    
