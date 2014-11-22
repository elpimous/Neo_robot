#!/usr/bin/env python
# Author: Derek Green

PKG = 'robbie'

import roslib; roslib.load_manifest(PKG)
import rospy

from std_msgs.msg import String

class TerminalInput():
    def __init__(self):
        self.pub = rospy.Publisher('speech_text', String)
        rospy.init_node('terminal_input_node', anonymous=True)
        print "ENTERING TERMINAL INPUT"
        while not rospy.is_shutdown():
            line = raw_input("Enter speech: ")
            self.pub.publish(line) # .rstrip('\n'))

if __name__ == '__main__':
    try:
        st = TerminalInput()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
