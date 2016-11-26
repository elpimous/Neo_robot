#!/usr/bin/python
# -*- coding: utf-8 -*-

########################################################################
#
# PACKAGE FOR QBO ROBOT ( ROS indigo version)
#
# node to detect a face with DLIB process
#
# publish to '/facial_detection' topic with strings : 'yes' or 'no'
#
# robot nose becomes green when seen face, and turns off when unseen.
#
# -----------------------------------------------------------------
#
# Creates a service '/listening' 
# to send request to qbo-listening-service
#
# Publishes the ROI (region of interest) of the seen face on '/ROI'
#
# Enjoy.
#
# Vincent FOUCAULT      November 2016       elpimous12@orange.fr
#
########################################################################

import subprocess
import rospy
import cv2
import cv2.cv as cv
import numpy as np
import imutils
import dlib
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from qbo_face_msgs.msg import FacePosAndDist
from sensor_msgs.msg import Image, RegionOfInterest
from qbo_arduqbo.msg import Nose
from qbo_listen.srv import Listening

class FaceDetection():
    def __init__(self):
        self.node_name = "neo_facesDetector"
        rospy.init_node(self.node_name)
        # Dlib detection mode
        self.detector = dlib.get_frontal_face_detector()
        # initialize a variable for a frame view
        # self.win = dlib.image_window()
        self.nose_pub = rospy.Publisher('/cmd_nose', Nose, queue_size=1)
        self.face_detection = rospy.Publisher('/facial_detection', String, queue_size=5)

        # Initialize the Region of Interest and its publisher
        #self.ROI = FacePosAndDist()
        self.ROI = RegionOfInterest()

        #self.roi_pub = rospy.Publisher("/qbo_face_tracking/face_pos_and_dist", FacePosAndDist, queue_size=1)
        self.roi_pub = rospy.Publisher("roi", RegionOfInterest, queue_size=1)

        self.no_nose_pub_done = False
        self.color_nose_pub_done = False

        self.data = "off"
        # Opencv/Ros bridge
        self.bridge = CvBridge()
        # subscribe to a ros topic to retrieve video flux
        self.image_sub = rospy.Subscriber("/stereo/left/image_raw", Image, self.image_callback, queue_size=10)
        # let program wait until subscribing is OK
        rospy.wait_for_message("/stereo/left/image_raw", Image)
        print "video stream OK..."

    # camera image from ROS camera topic
    def image_callback(self, ros_image):
        try:
            self.frame = self.bridge.imgmsg_to_cv2(ros_image,"rgb8")
            self.gray_frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            self.resized_frame = cv2.resize(self.gray_frame, (0,0), fx=0.5, fy=0.5)
            self.frame = self.resized_frame

            dets = self.detector(self.frame, 1)
            self.faces = int(len(dets))

            # green nose
            if self.faces > 0 and not self.color_nose_pub_done:
                self.color_nose_pub_done = True
                self.no_nose_pub_done = False
                self.Nose(2)
                self.data = "oui"
                self.face_detection.publish(self.data)
                
                try :
                    self.Sending_listening_switch(self.data)
                except : pass
                """

                for i, d in enumerate(dets):
                    roi = (i, d.left(), d.top(), d.right(), d.bottom())
                    x = int(roi[1])
                    y = int(roi[2])
                    w = int(roi[3])
                    h = int(roi[4])

                    # j'ai un peu triché avec les valeurs, pour pallier au décalage de l'oeil gauche
                    self.ROI.x_offset = (x+w)/2-(100) # moitié de l'écran horiz
                    self.ROI.y_offset = (y+h)/2-(70) # moitié de l'écran vert
                    print self.ROI.x_offset, self.ROI.y_offset
                    #self.ROI.distance_to_head = 0.79
                    #self.ROI.image_width = 160
                    #self.ROI.image_height = 120
                    self.roi_pub.publish(self.ROI)

                """

            # no nose color
            if self.faces == 0 and not self.no_nose_pub_done:
                self.no_nose_pub_done = True
                self.color_nose_pub_done = False
                self.data = "non"
                self.face_detection.publish(self.data)
                try :
                    self.Sending_listening_switch(self.data)
                except : pass

                self.Nose(0)

            else:
                pass

        except : pass

    # change color nose function
    def Nose(self, color_value):
        nose_command=Nose()
        nose_command.color = color_value
        self.nose_pub.publish(nose_command)

    def run_process(self, command = ""):
        if command != "":
            return subprocess.Popen(command.split())
        else:
            return -1

    def Sending_listening_switch(self, value):
    	try:
            self.run_process('rosservice call /listening '+str(value))
        except : pass


if __name__ == '__main__':
    try:
        a = FaceDetection()
        rospy.spin()
    except rospy.ROSInterruptException: pass
