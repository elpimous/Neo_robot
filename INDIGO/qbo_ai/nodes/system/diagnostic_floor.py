#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" qbo_floorSensor.py - Version 1.0 2015-09-11

    Created for Jarvis Project
    Authors: Sylvain Zwolinski <sylvain-zwolinski@orange.fr>
    
"""
import roslib
import rospy
import os

from sensor_msgs.msg import PointCloud

from diagnostic_msgs.msg import *
from lib_qbo_pyarduqbo import qbo_control_client


class DiagnosticFloor:

    def __init__(self):
        
        rospy.init_node('DiagnosticFloor')
        
        # The rate at which to publish the diagnostic sensor floor
        self.rate = rospy.get_param("~rate", 1)
        
        # Convert to a ROS rate
        r = rospy.Rate(self.rate)
        
        self.qbo_controller=qbo_control_client()
        
        
        # Create a diagnostics publisher
        diag_pub = rospy.Publisher("diagnostics", DiagnosticArray)
        
         # Initialize the min and the max alert distance to the params Qbo_arduqbo (in m)
        floor_min = rospy.get_param("/qbo_arduqbo/controllers/sens_con/sensors/floor/floor_sensor/min_alert_distance")   
        floor_max = rospy.get_param("/qbo_arduqbo/controllers/sens_con/sensors/floor/floor_sensor/max_alert_distance")
        
        #print floor_min
        #print floor_max
        
        rospy.loginfo("Publishing diagnostic message from the floor sensor")
        
        while not rospy.is_shutdown():
            
            
            # Initialize the diagnostics status
            status = DiagnosticStatus()
            status.name = "Floor Sensor"
            status.hardware_id = "Sensors"
            
            getFloorSensor = self.qbo_controller.getFloorSensor()
            #print getFloorSensor
            distanceFloor = "%.2f" %getFloorSensor[0][0]
            #print distanceFloor
            
            if getFloorSensor[0][0] > floor_max :
                status.message = "Alert Floor Sensor"
                status.level = DiagnosticStatus.WARN
                                
            elif getFloorSensor[0][0] < floor_min :
                status.message = "Alert Floor Sensor"
                status.level = DiagnosticStatus.WARN
               
            else:
                status.message = "Floor Sensor OK"
                status.level = DiagnosticStatus.OK
                now=rospy.Time.now()
            
            # Add the raw floor sensor and limits to the diagnostics message
            status.values.append(KeyValue("Floor sensor", str(distanceFloor)))
            status.values.append(KeyValue("floor_min", str(floor_min)))
            status.values.append(KeyValue("floor_max", str(floor_max)))
            
            # Build the diagnostics array message
            msg = DiagnosticArray()
            msg.header.stamp = rospy.Time.now()
            msg.status.append(status)
            
            diag_pub.publish(msg)
            
            r.sleep()

if __name__ == '__main__':
   DiagnosticFloor()
   
