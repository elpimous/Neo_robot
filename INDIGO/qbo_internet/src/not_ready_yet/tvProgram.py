#!/usr/bin/env python
# coding: utf-8


# Author: Vincent FOUCAULT
# use of web TV program api, for robot speech at demand
# end march 2016


import rospy
import requests
import urllib2
import json

# enter here your PERSONAL KEY
myKey = ""

# TV program, this day
tonight = urllib2.urlopen('http://api....')
json_string = tonight.read()
parsed_json = json.loads(json_string)
ch1 = parsed_json['']
ch2 = parsed_json['']
ch3 = parsed_json['']
ch5 = parsed_json['']
ch6 = parsed_json['']
ch8 = parsed_json['']
ch9 = parsed_json['']


# TV program, tomorrow night
tomorrow = urllib2.urlopen('http://api....')
json_string2 = tomorrow.read()
parsed_json2 = json.loads(json_string2)
ch1_tomorrow = parsed_json['']
ch2_tomorrow = parsed_json['']
ch3_tomorrow = parsed_json['']
ch5_tomorrow = parsed_json['']
ch6_tomorrow = parsed_json['']
ch8_tomorrow = parsed_json['']
ch9_tomorrow = parsed_json['']

def Tonight():
    print "Ce soir, sur TF1, %s. Sur la deux, %s. Sur la trois, %s. Sur la cinq, %s. Sur M6, %s. Sur la huit, %s. Sur W9, %s." % (str(ch1), str(ch2), str(ch3), str(ch5), str(ch6), str(ch8), str(ch9)) 
    f.close()

def Tomorrow():
    print "Demain soir, sur TF1, %s. Sur la deux, %s. Sur la trois, %s. Sur la cinq, %s. Sur M6, %s. Sur la huit, %s. Sur W9, %s." % (str(ch1_tomorrow), str(ch2_tomorrow), str(ch3_tomorrow), str(ch5_tomorrow), str(ch6_tomorrow), str(ch8_tomorrow), str(ch9_tomorrow))
    forecast.close()


if __name__ == '__main__':

    rospy.init_node("qbo_tv_program")
    try:
        tonight = Tonight()
        tomorrow = Tomorrow()
        #rospy.spin()
    except rospy.ROSInterruptException: pass


