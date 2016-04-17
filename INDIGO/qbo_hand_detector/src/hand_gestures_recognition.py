#!/usr/bin/env python
# -*- coding: utf-8 -*-

###########################################
# Hand gestures program, working as switch
# ROS indigo / Mint 17.3
# vincent FOUCAULT 03 avril 2016
###########################################

import rospy
import cv2
import cv2.cv as cv
import math
import numpy as np
import time
from time import sleep
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


class cvBridge():
    def __init__(self):
        self.node_name = "qbo_hand_gesture"
        rospy.init_node(self.node_name)
        rospy.on_shutdown(self.cleanup)
        # How often should we update the robot's motion?
        #self.cv_window_name = self.node_name
        #cv.NamedWindow(self.cv_window_name, cv.CV_WINDOW_NORMAL)
        #cv.MoveWindow(self.cv_window_name, 25, 75)
        self.bridge = CvBridge()
        self.pub = rospy.Publisher('/hand_detector', String, queue_size=10)
        self.image_sub = rospy.Subscriber("/stereo/right/image_raw", Image, self.image_callback, queue_size=1)
        #rospy.loginfo("Waiting for image topics...")
        rospy.wait_for_message("/stereo/right/image_raw", Image)
        #rospy.loginfo("Looking for hand gesture...")


    def image_callback(self, ros_image):
            try:
                self.frame_orig = self.bridge.imgmsg_to_cv2(ros_image, "bgr8")
            except CvBridgeError, e:
                print e
            self.frame = np.array(self.frame_orig, dtype=np.uint8)
            img = self.frame

            # Thanks to vipul-sharma for hand process !!
            # http://github.com/vipul-sharma20/

            cv2.rectangle(img,(20,10),(300,230),(0,255,0),0)
            crop_img = img[0:300, 0:300]
            grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            value = (35, 35) # 35
            blurred = cv2.GaussianBlur(grey, value, 0)
            _, thresh1 = cv2.threshold(blurred, 127, 255,
                               cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            #cv2.imshow('Thresholded', thresh1)
            contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
                    cv2.CHAIN_APPROX_NONE)
            max_area = -1
             
            for i in range(len(contours)):
                cnt=contours[i]
                area = cv2.contourArea(cnt)
                if(area>max_area):
                    max_area=area
                    ci=i
            cnt=contours[ci]
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
            hull = cv2.convexHull(cnt)
            drawing = np.zeros(crop_img.shape,np.uint8)
            cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
            cv2.drawContours(drawing,[hull],0,(0,0,255),0)
            hull = cv2.convexHull(cnt,returnPoints = False)
            defects = cv2.convexityDefects(cnt,hull)
            count_defects = 0
            cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
                if angle <= 90:
                    count_defects += 1
                    cv2.circle(crop_img,far,1,[0,0,255],-1)
                cv2.line(crop_img,start,end,[0,255,0],2)

            # Here is the "button" / pass tour hand between 50 to 7 cm from rignt eye
            if count_defects >= 4 :
                #print "vu"
                self.SeenHand = "seen"
            elif count_defects < 3 :
                self.SeenHand = "unseen"
            self.pub.publish(str(self.SeenHand))

            #cv2.imshow('drawing', drawing)
            #cv2.imshow('end', crop_img)
            #cv2.imshow(self.node_name, img)
            #all_img = np.hstack((drawing, crop_img))
            #cv2.imshow('Contours', all_img)
            #k = cv2.waitKey(10)


    def ICU(self):
        return self.SeenHand


    def cleanup(self):
        print "Shutting down hand_gesture node."
        cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        cvBridge = cvBridge()
        cvBridge.ICU()
        rospy.spin()
    except rospy.ROSInterruptException: pass
