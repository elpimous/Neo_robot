#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
*************************************************************************
                         Vincent FOUCAULT       January 2016
*************************************************************************
'''

import os, rospy, subprocess
from std_msgs.msg import String


def run_process(command = ""):
    if command != "":
        return subprocess.Popen(command.split())
    else:
        return -1


class GoingToCharge():

    def __init__(self):
        rospy.Subscriber('chargeNeeded', String, self.ChargeNeeded)
        self.done = False

    def ChargeNeeded(self,msg):
        self.chargeNeeded = msg.data
        if self.chargeNeeded == 'yes' and not self.done:
          rospy.loginfo('Je démarre la localisation de ma base de recharge')
          run_process('roslaunch qbo_return_home return_home.launch')
          self.done = True
        else :
          pass
        

if __name__ == '__main__':
    try:
        rospy.init_node("GoingToCharge")
        GoingToCharge()
        rospy.spin()
    except rospy.ROSInterruptException:
        rospy.loginfo("RTH node terminated.")
