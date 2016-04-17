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

class DiagnosticBackLeft:
  
    def __init__(self):
    
        rospy.init_node('DiagnosticBackLeft')
    
        self.qbo_controller=qbo_control_client()
    
        # The rate at which to publish the diagnostic sensor back left
        self.rate = rospy.get_param("~rate", 1)
    
        # Convert to a ROS rate
        self.r = rospy.Rate(self.rate)
       
        # Initialize the min alert distance to the params Qbo_arduqbo (in m)
        self.alert_back_left = rospy.get_param("/qbo_arduqbo/controllers/sens_con/sensors/back/back_left_srf10/min_alert_distance")
        
        # Create a diagnostics publisher
        self.diag_pub_L = rospy.Publisher("diagnostics", DiagnosticArray)

    def backDistanceLeft(self):
        
        while not rospy.is_shutdown():
            
            # Initialize the diagnostics status
            status = DiagnosticStatus()
            status.name = "Back Distance Left"
            status.hardware_id = "Sensors"
            
            BackDistances = self.qbo_controller.getBackDistances()
            now=rospy.Time.now()
            left_sensor = 0.0
          
            if BackDistances[0][1] and (now-BackDistances[0][1])<rospy.Duration(0.5):
                left_sensor = "%.2f" %BackDistances[0][0]
                
                if str(left_sensor) <= str(self.alert_back_left) :
                    status.message = "Alert Collision Back Left"
                    status.level = DiagnosticStatus.WARN
                else :
                    status.message = "Obstacle detected Back Left"
                    status.level = DiagnosticStatus.OK
            else:
                status.message = "Sensor Back Left OK"
                status.level = DiagnosticStatus.OK
            
                        
            # Add the raw floor sensor and limits to the diagnostics message
            status.values.append(KeyValue("Back left value", str(left_sensor)))
            status.values.append(KeyValue("Value alert", str(self.alert_back_left)))
            
            
            # Build the diagnostics array message
            msg = DiagnosticArray()
            msg.header.stamp = rospy.Time.now()
            msg.status.append(status)
            
            self.diag_pub_L.publish(msg)
            
            self.r.sleep()

if __name__ == '__main__':
   node = DiagnosticBackLeft()
   node.backDistanceLeft()
