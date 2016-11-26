#!/usr/bin/env python
# -*- coding: utf-8 -*-


#********************************************************************
#
#
#                 QBO LISTEN USING POCKETSPHINX
#
#                REALLY USEFULL FOR VOCAL ORDERS
#
#              USE LISTEN_GOOGLE NODE FOR BETTER DIC
#
#                     elpimous12@orange.fr
#
#
#********************************************************************

import rospy
import subprocess
import pocketsphinx as ps
import sphinxbase
from std_msgs.msg import String
import commands


# record location
audio_file = '/tmp/recording.wav' 

# recording process, use of SOX, 1 channel, rate 16000, default qbo audio config
# silence used to create blank sounds before and after record
record = 'sox -c 1 -r 16000 -t alsa default "'+audio_file+'" silence 1 0.1 1% 1 1.5 1%' 

class recognizer(object):
    
    def __init__(self):

        rospy.init_node("qbo_listen")
        hmdir=rospy.get_param("~hmm")
        lmd=rospy.get_param("~lm")
        dictd=rospy.get_param("~dict")

        while not rospy.is_shutdown():

            def decodeSpeech(hmdir,lmd,dictd,audio_file):

                # pocketsphinx wav recognition process. Do not modify !
                subprocess.call(record, shell=True)
                speechRec = ps.Decoder(hmm = hmdir, lm = lmd, dict = dictd)
                audio_file2 = file(audio_file,'rb')
                audio_file2.seek(44)
                speechRec.decode_raw(audio_file2)
                result = speechRec.get_hyp()
                return result[0] 

            recognised = decodeSpeech(hmdir,lmd,dictd,audio_file)
            recognised = str(recognised) # to avoid python error on printing "none object"
            print""
            print'        Ai-je bien compris : "'+recognised+'" ?...'
            print""

            # publishing sentence in "/listened" topic
            pub = rospy.Publisher('listened', String, queue_size=10)
            pub.publish(recognised)
            continue

if __name__ == "__main__":
    start = recognizer()

