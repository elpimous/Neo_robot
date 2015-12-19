#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#########################################################################################
#	                                      						#
#             USE OF GOOGLE TEXT TO SPEECH API V2 FOR QBO OPEN-SOURCE ROBOT             #
#											#
#                           YOU NEED TO CREATE YOUR OWN API KEY                         #
#                                                                                       #
#                    http://www.chromium.org/developers/how-tos/api-keys                #
#											#
#											#
#                          Vincent FOUCAULT, elpimous12@orange.fr                       #
#											#
#########################################################################################


# requests are limited to 15 seconds (one hack exists for that)
# requests are limited to 50 per 24h (no hack for that, but some guys recover key on windows or ubuntu web browser...)
# on a slow net connection, i have response under 2 to 3 sec. A bit slow for now, but it's better than nothing and it's the best speech recognition

# permit use of utf8 standard use (needed for french decoding)
from __future__ import unicode_literals

import rospy
from std_msgs.msg import String
import shlex,subprocess,os

# Voice recording at 16000 and mono wav, for speedup recognition.
REC = 'rec --encoding signed-integer --bits 16 --channels 1 --rate 16000 recording.wav silence 1 0.1 1% 1 1.5 1%'

# Need personal chromium Key for only google speech api : V2 one. (V1 finished !)
private_api_key='XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"'	
# Selection of language recognition language                                    						
selected_language="fr-fr"
# Api V2 request
REQ='wget -O - -o /dev/null --post-file recording.wav --header="Content-Type: audio/l16; rate=16000" "https://www.google.com/speech-api/v2/recognize?output=json&lang='+selected_language+"&key="+private_api_key+' > /home/neo/Documents/texte.txt'


class recognizer(object):
    
    def __init__(self):

        rospy.init_node("qbo_listen")

        while not rospy.is_shutdown():

            def speech():

		os.system(REC)
                #os.remove ("/tmp/listened.txt")
		subprocess.Popen(REQ, shell=True, stdout=subprocess.PIPE).communicate()

                fichier_texte =  open('/home/neo/Documents/texte.txt', 'r').read().decode('utf-8')

                if len(fichier_texte)>=30:

                    sentence = fichier_texte.split('"transcript":')[1].split(',')[0].replace('"','').replace('}','')
                    print sentence
                    # publishing sentence in "/listened" topic
        	    pub = rospy.Publisher('listened', String, queue_size=1)
        	    pub.publish(sentence) 

                else:

                    print "rien à décoder !"

            speech()


if __name__ == "__main__":
    start = recognizer()

