#!/usr/bin/env python

import roslib
roslib.load_manifest('pi_head_tracking_tutorial')
import sys
import rospy
import cv
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class vision_node:

    def __init__(self):
        rospy.init_node('vision_node')

        self.cv_window_name = "OpenCV Image"

        cv.NamedWindow(self.cv_window_name, 1)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/camera/rgb/image_color", Image, self.callback)

    def callback(self, data):
        try:
          cv_image = self.bridge.imgmsg_to_cv(data, "bgr8")
        except CvBridgeError, e:
          print e
   
        cv.ShowImage(self.cv_window_name, cv_image)
        cv.WaitKey(3)

def main(args):
      vn = vision_node()
      try:
        rospy.spin()
      except KeyboardInterrupt:
        print "Shutting down vison node."
        cv.DestroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)
