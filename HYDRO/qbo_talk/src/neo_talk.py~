#!/usr/bin/env python
# coding: utf-8
# Author: Vincent FOUCAULT
# Here is a text-to-speech wrapper for Espeak
# It's part of QBO robot ros softwares


import roslib; roslib.load_manifest('qbo_talk')
import rospy
from qbo_talk.srv import Text2Speach # read service content (words we want to be spoken)
import os

# Some possibilities of different languages
fr_speak = "espeak -a 70 -s 140 -p50 -v mb/mb-fr1 \"%s\" | mbrola -e -C \"n n2\" /usr/share/mbrola/voices/fr1 - -.au | paplay"
en_speak = "espeak -a 70 -s 140 -p50 -v mb/mb-en1 \"%s\" | mbrola -e -C \"n n2\" /usr/share/mbrola/voices/en1 - -.au | paplay"
es_speak = "espeak -a 70 -s 140 -p50 -v mb/mb-es1 \"%s\" | mbrola -e -C \"n n2\" /usr/share/mbrola/voices/es1 - -.au | paplay"

class talk():
    def __init__(self):
        rospy.init_node('talk', anonymous=True)
        s = rospy.Service('say', Text2Speach, self.Qbo_talk) # create a new service called "/say" (you can see them here : rosservice list)
    def Qbo_talk(self, speak):
        os.system(fr_speak % speak.sentence) # just replace "fr" to en or es...
        return []

if __name__ == '__main__':
    try:
        talk = talk()
        rospy.spin()
    except rospy.ROSInterruptException: pass


