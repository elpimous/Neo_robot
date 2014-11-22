#!/usr/bin/env python

import roslib; roslib.load_manifest('rviz')
import rospy
import os

os.system("rosrun rviz rviz -d 'rospack find New_qbo_urdf' /qbo_nav_setup_rviz.vcg")

