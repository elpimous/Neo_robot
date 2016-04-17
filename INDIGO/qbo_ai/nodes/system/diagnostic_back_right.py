#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" DiagnosticSensors.py - Version 1.0 2015-09-17

    Created for Jarvis Project
    Authors: Sylvain Zwolinski <sylvain-zwolinski@orange.fr>
    
"""

import roslib
import rospy
import os


from sensor_msgs.msg import PointCloud
from qbo_talk.srv import Text2Speach
from qbo_manager.srv import Text2Write
from diagnostic_msgs.msg import *
from lib_qbo_pyarduqbo import qbo_control_client

class DiagnosticBackRight:
  
    def __init__(self):
    
        rospy.init_node('DiagnosticBackRight')
    
        self.qbo_controller=qbo_control_client()
    
        # The rate at which to publish the diagnostic sensor back right
        self.rate = rospy.get_param("~rate", 1)
    
        # Convert to a ROS rate
        self.r = rospy.Rate(self.rate)
       
        # Initialize the min alert distance to the params Qbo_arduqbo (in m)
        self.alert_back_right = rospy.get_param("/qbo_arduqbo/controllers/sens_con/sensors/back/back_right_srf10/min_alert_distance")
        
        # Create a diagnostics publisher
        self.diag_pub_R = rospy.Publisher("diagnostics", DiagnosticArray)

    def backDistanceRight(self):
        
        while not rospy.is_shutdown():
            
            # Initialize the diagnostics status
            status = DiagnosticStatus()
            status.name = "Back Distance Right"
            status.hardware_id = "Sensors"
            
            BackDistances = self.qbo_controller.getBackDistances()
            now=rospy.Time.now()
            right_sensor = 0.0
                       
            if BackDistances[1][1] and (now-BackDistances[1][1])<rospy.Duration(0.5):
                right_sensor = "%.2f" %BackDistances[1][0]
                if str(right_sensor) <= str(self.alert_back_right) :
                    status.message = "Alert Collision Back Right"
                    status.level = DiagnosticStatus.WARN
                else :
                    status.message = "Obstacle detected back right"
                    status.level = DiagnosticStatus.OK
            else:
                status.message = "Sensor back right OK"
                status.level = DiagnosticStatus.OK
            
                        
            # Add the raw floor sensor and limits to the diagnostics message
            status.values.append(KeyValue("Back right value", str(right_sensor)))
            status.values.append(KeyValue("Value alert", str(self.alert_back_right)))
            
            
            # Build the diagnostics array message
            msg = DiagnosticArray()
            msg.header.stamp = rospy.Time.now()
            msg.status.append(status)
            
            self.diag_pub_R.publish(msg)
            
            self.r.sleep()

if __name__ == '__main__':
   node = DiagnosticBackRight()
   node.backDistanceRight()
