#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
from sensor_msgs.msg import Joy

import time
import sys, tty, termios

class JoyCtrl:
	def __init__(self):
		self.axis_wheel_straight = rospy.get_param('axis_wheel_straight', 1)
		self.axis_wheel_turn = rospy.get_param('axis_wheel_turn', 2)
		self.axis_head_pan = rospy.get_param('axis_head_pan', 4)
		self.axis_head_tilt = rospy.get_param('axis_head_tilt', 3)
		self.button_nose = rospy.get_param('button_nose', 14)

		self.pub_base = rospy.Publisher('/cmd_vel', Twist)
		self.pub_joints = rospy.Publisher('/cmd_joints',JointState)
		
		self.sub_joy = rospy.Subscriber('/joy', Joy, self.joy_cb)
		self.sub_joint = rospy.Subscriber('/joint_states', JointState, self.joint_cb)

	def joy_cb(self, data):
		self.move_base(self.pub_base, data.axes[self.axis_wheel_straight]*0.5, data.axes[self.axis_wheel_turn])
		self.move_head(self.pub_joints, data.axes[self.axis_head_tilt], data.axes[self.axis_head_pan])

	def joint_cb(self, data):
		self.head_tilt_pos = data.position[3]
		self.head_pan_pos = data.position[2]
		

	def move_base(self, publisher, linear, ang):
		speed_command=Twist()
		speed_command.linear.x=linear
		speed_command.linear.y=0
		speed_command.linear.z=0
		speed_command.angular.x=0
		speed_command.angular.y=0
		speed_command.angular.z=ang
		publisher.publish(speed_command)

	def move_head(self, publisher, speed_tilt, speed_pan):
		servo_command=JointState()
		servo_command.name=['head_tilt_joint', 'head_pan_joint']
		tilt_pos = self.head_tilt_pos
		pan_pos = self.head_pan_pos
	
		if speed_tilt > 0:
			tilt_pos -= 0.2
		elif speed_tilt < 0:
			tilt_pos += 0.2
	
		if speed_pan > 0:
			pan_pos -= 0.2
		elif speed_pan < 0:
			pan_pos += 0.2
	
		servo_command.position=[tilt_pos, pan_pos]
	
		publisher.publish(servo_command)
		

def main():
	rospy.init_node('qbo_joy_control')

	c = JoyCtrl()

	rospy.spin()	

if __name__ == "__main__":
	main()
