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

def speak_this(text): 
  global client_speak
  client_speak(str(text))

def run_process(command = ""):
    if command != "":
        return os.system(command)
    else:
        return -1

   
class DiagnosticFrontRight:
  
    def __init__(self):
    
        rospy.init_node('DiagnosticFrontRight')
    
        self.qbo_controller=qbo_control_client()
    
        # The rate at which to publish the diagnostic sensor front right
        self.rate = rospy.get_param("~rate", 1)
    
        # Convert to a ROS rate
        self.r = rospy.Rate(self.rate)
         
        # Initialize the min alert distance to the params Qbo_arduqbo (in m)
        self.alert_front_right = rospy.get_param("/qbo_arduqbo/controllers/sens_con/sensors/front/front_right_srf10/min_alert_distance")
          
        client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
    
        #service_manager = rospy.ServiceProxy('manager', Text2Write)
    
        # Create a diagnostics publisher
        self.diag_pub_R = rospy.Publisher("diagnostics", DiagnosticArray, queue_size = 1)

    def frontalDistanceRight(self):
        
        while not rospy.is_shutdown():
            
            # Initialize the diagnostics status
            status = DiagnosticStatus()
            status.name = "Frontal Distances Right"
            status.hardware_id = "Sensors"
            
            FrontalDistances = self.qbo_controller.getFrontalDistances()
            now=rospy.Time.now()
            right_sensor = 0.0
                                    
            if FrontalDistances[1][1] and (now-FrontalDistances[1][1])<rospy.Duration(0.5):
                right_sensor = "%.2f" %FrontalDistances[1][0]
                if str(right_sensor) <= str(self.alert_front_right) :
                    status.message = "Alert Collision Front Right"
                    status.level = DiagnosticStatus.WARN
                else :
                    status.message = "Obstacle detected front right"
                    status.level = DiagnosticStatus.OK
            else:
                status.message = "Sensor front right OK"
                status.level = DiagnosticStatus.OK    
            
            # Add the raw right sensor and limit to the diagnostics message
            status.values.append(KeyValue("Front right value", str(right_sensor)))
            status.values.append(KeyValue("Value alert", str(self.alert_front_right)))
            
            # Build the diagnostics array message
            msg = DiagnosticArray()
            msg.header.stamp = rospy.Time.now()
            msg.status.append(status)
            
            self.diag_pub_R.publish(msg)
            
            self.r.sleep()

if __name__ == '__main__':
   node = DiagnosticFrontRight()
   node.frontalDistanceRight()
   
