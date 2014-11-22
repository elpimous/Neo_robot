#!/usr/bin/env python

import roslib; roslib.load_manifest('rviz')
import rospy
import os

os.system("rosrun rviz rviz -d 'rospack find rbx1_nav' /amcl.rviz")

