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
from diagnostic_msgs.msg import *
from lib_qbo_pyarduqbo import qbo_control_client

class DiagnosticFrontLeft:
  
    def __init__(self):
    
        rospy.init_node('DiagnosticFrontLeft')
    
        self.qbo_controller=qbo_control_client()
    
        # The rate at which to publish the diagnostic sensor front left
        self.rate = rospy.get_param("~rate", 1)
    
        # Convert to a ROS rate
        self.r = rospy.Rate(self.rate)
       
        # Initialize the min alert distance to the params Qbo_arduqbo (in m)
        self.alert_front_left = rospy.get_param("/qbo_arduqbo/controllers/sens_con/sensors/front/front_left_srf10/min_alert_distance")
        
        # Create a diagnostics publisher
        self.diag_pub_L = rospy.Publisher("diagnostics", DiagnosticArray, queue_size = 1)

    def frontalDistanceLeft(self):
        
        while not rospy.is_shutdown():
            
            # Initialize the diagnostics status
            status = DiagnosticStatus()
            status.name = "Frontal Distances Left"
            status.hardware_id = "Sensors"
            
            FrontalDistances = self.qbo_controller.getFrontalDistances()
            now=rospy.Time.now()
            left_sensor = 0.0
                       
            if FrontalDistances[0][1] and (now-FrontalDistances[0][1])<rospy.Duration(0.5):
                left_sensor = "%.2f" %FrontalDistances[0][0]
                if str(left_sensor) <= str(self.alert_front_left) :
                    status.message = "Alert Collision Front Left"
                    status.level = DiagnosticStatus.WARN
                else :
                    status.message = "Obstacle detected front left"
                    status.level = DiagnosticStatus.OK
            else:
                status.message = "Sensor front left OK"
                status.level = DiagnosticStatus.OK
            
                        
            # Add the raw floor sensor and limits to the diagnostics message
            status.values.append(KeyValue("Front left value", str(left_sensor)))
            status.values.append(KeyValue("Value alert", str(self.alert_front_left)))
            
            
            # Build the diagnostics array message
            msg = DiagnosticArray()
            msg.header.stamp = rospy.Time.now()
            msg.status.append(status)
            
            self.diag_pub_L.publish(msg)
            
            self.r.sleep()

if __name__ == '__main__':
   node = DiagnosticFrontLeft()
   node.frontalDistanceLeft()
