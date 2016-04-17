#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################
#
#  opencv receives the video topic stream,
#  search ball color (red/green/blue)
#  color is published in topic : /ball_color
#
#                   Vincent FOUCAULT 6 APRIL 2016
######################################################################

import rospy
import math
import random
import cv2
import cv2.cv as cv
import numpy as np
import imutils
import sys
from threading import Thread
from sensor_msgs.msg import Image
from std_msgs.msg import String
from cv_bridge import CvBridge, CvBridgeError

class colorGame():
    def __init__(self):
        self.node_name = "qbo_color_balls_publisher"
        rospy.init_node(self.node_name)
        #rospy.on_shutdown(self.cleanup)
        self.cv_window_name = self.node_name
        cv.NamedWindow(self.cv_window_name, cv.CV_WINDOW_NORMAL)
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber("/stereo/left/image_raw", Image, self.image_callback, queue_size=20)
        rospy.wait_for_message("/stereo/left/image_raw", Image)
        self.pub = rospy.Publisher('/ball_color', String, queue_size=1)
        self.rouge = ""
        self.verte = ""
        self.bleue = ""
        print "video stream ok..."

    def image_callback(self, ros_image):
        try:
            self.BGR_frame = self.bridge.imgmsg_to_cv2(ros_image,"bgr8")

        except CvBridgeError, e:
            print e
        self.frame = cv2.cvtColor(self.BGR_frame, cv2.COLOR_BGR2HSV)
        # launch threading process
        self.start()

    def start(self):
	# start the thread to read frames from the video stream
	Thread(target=self.process, args=()).start()
	return self

    def process(self):
        self.rate = rospy.get_param("~rate", 5)
        self.r = rospy.Rate(self.rate) 
        self.frame = np.array(self.frame, dtype=np.uint8)

        # resizing to speedup processes
        # blurring
	#self.frame = cv2.GaussianBlur(self.frame, (11, 11), 0) # no interest here !!!

	# define the 3 balls color, low and high limit values in HSV
	self.colors_mask_HSV = [
		(["verte"], [74, 96, 66], [97, 199, 170]),
		(["bleue"], [107,107,147], [113,206,255]),
		(["rouge"], [172,103,169], [177,179,206])
		      ]

	# loop from colors, to find asked one, and keep it's values
	for (color, lower, upper) in self.colors_mask_HSV:
                # name of actual color mask (searched color)
                self.color_name = str(color).replace('[','').replace("'","").replace("]","")
		lower = np.array(lower, dtype = "uint8")
		upper = np.array(upper, dtype = "uint8")
                # target color mask with low and high color range values
                # better results in low luminosity with HSV colors
		self.mask = cv2.inRange(self.frame, lower, upper)
                # remove any small blobs
	        self.mask = cv2.erode(self.mask, None, iterations=2)
	        self.mask = cv2.dilate(self.mask, None, iterations=2)
                """
                # find contours in the mask and initialize the current
		# (x, y) center of the ball ("-2" for opencv3 compatibility)
		cnts = cv2.findContours(self.mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
		center = None
	        # only proceed if at least one contour was found
		if len(cnts) > 0:
			# find the largest contour in the mask, then use
			# it to compute the minimum enclosing circle and
			# centroid
			c = max(cnts, key=cv2.contourArea)
			((x, y), radius) = cv2.minEnclosingCircle(c)
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			# only proceed if the radius meets a minimum size
			if radius > 5:
				# draw the circle and centroid on the frame,
				# then update the list of tracked points
				cv2.circle(self.frame, (int(x), int(y)), int(radius),
					(0, 255, 255), 2)
                """
		output = cv2.bitwise_and(self.frame, self.frame, mask = self.mask)
		# search  for mask color pixels in picture
		colorPixelMaskCount = cv2.inRange(self.frame, lower, upper)
                # count mask color pixels in picture
		howManyPix = cv2.countNonZero(colorPixelMaskCount)
                font = cv2.FONT_HERSHEY_SIMPLEX
                # if a color appears at a certain pixels value, put it on variable !
                if howManyPix >= 1500: # 600 or more pixels of "selected mask" in picture
                	ballColor = self.color_name
                        self.pub.publish(ballColor)
                        """
                        if ballColor == "rouge":
                            self.rouge = howManyPix
                        if ballColor == "verte":
                            self.verte = howManyPix
                        if ballColor == "bleue":
                            self.bleue = howManyPix
                        """

                if howManyPix < 1500:
                    try:
                        self.pub.publish("no_color")
                        #print " no color !!!"
                    except:
                        print " impossible de publier"
                        pass

                if self.color_name == "rouge":
                    cv2.putText(self.BGR_frame,self.color_name,(10,30), font, 1,(0,0,255),2)
                if self.color_name == "verte":
                    cv2.putText(self.BGR_frame,self.color_name,(10,230), font, 1,(0,255,0),2)
                if self.color_name == "bleue":
                    cv2.putText(self.BGR_frame,self.color_name,(220,30), font, 1,(255,0,0),2)

		#cv2.imshow(self.node_name, np.hstack([self.BGR_frame, output]))
	        #k = cv2.waitKey(15)

        """
        # find best color in a loop (if more than one seen !)
        self.best_color = max(self.rouge,self.verte,self.bleue)
        if self.best_color == self.rouge:
            ballColor = "rouge"
        if self.best_color == self.verte:
            ballColor = "verte"
        if self.best_color == self.bleue:
            ballColor = "bleue"
        self.pub.publish(ballColor)
        print "je vois la balle : "+ballColor
        """
        # Sleep for 1/self.rate seconds
        self.r.sleep() #  refresh 2 times per second

    #def cleanup(self):
        #print "\nLeaving game"
        #cv2.destroyAllWindows()

if __name__ == '__main__':
    try:
        a = colorGame()
        rospy.spin()
    except rospy.ROSInterruptException: pass










