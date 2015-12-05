#!/usr/bin/env python
# -*- coding: utf-8 -*-


#********************************************************************
#
#
#        ARTIFICIAL INTELLIGENCY WITH PY-AIML (ALICE STYLE)
#
#                 KEYBOARD INPUTS FOR QUESTIONS
#
#                   ANSWER SPOKEN WITH QBO_TALK
#
#                    elpimous12@orange.fr
#
#
#********************************************************************

import rospy
from qbo_talk.srv import Text2Speach
from std_msgs.msg import String
import aiml_en
import sys

def speak_this(text): # for qbo_talk
    global client_speak
    client_speak(str(text))

class Neo_Chat():

    def __init__(self):
	global client_speak
        rospy.Subscriber('listened', String, self.listen_callback)
        client_speak = rospy.ServiceProxy("/say_en1", Text2Speach)
        rospy.init_node('neo_chat_node', anonymous=True)
        self.NEO = aiml_en.Kernel()# load AI
        self.brainLoaded = False # False to reload all aiml files !!!
        self.forceReload = False # force reload of all aiml files or when changes
	# personnal values
        self.NEO.setBotPredicate('name', "Neo")
        self.NEO.setBotPredicate('age' ,"environ six ans")
        self.NEO.setBotPredicate('anniversaire', "octobre 2014")
        self.NEO.setBotPredicate('gender', "garsson")
        self.NEO.setBotPredicate('master', "Vincent")
        self.NEO.setBotPredicate('favoritebook', "ROS par l'exemple")
        self.NEO.setBotPredicate('favcolor', "bleu")
        self.NEO.setBotPredicate('location' ,"France, dans l'Eure")
        self.NEO.setBotPredicate('sign', "taureau")
        self.NEO.setBotPredicate('favoritefood', "les ampères")
        self.NEO.setBotPredicate('favmovie', "Les temps modernes")
        self.NEO.setBotPredicate('favoriteband', "aucune")
        self.NEO.setBotPredicate('kindmusic', "aucune")
        self.NEO.setBotPredicate('birthplace' ,"France, dans l'Eure")

        while not self.brainLoaded:
	    if self.forceReload or (len(sys.argv) >= 2 and sys.argv[1] == "reload"):
		    self.NEO.bootstrap(learnFiles="/home/neo/catkin_ws/src/qbo_ai/ai_en/*.aiml")# load each aiml files, if self.forceReload is True (L38)
		    self.brainLoaded = False


		    # makes binary file, who contains all aiml files, for fast reboot
		    self.NEO.saveBrain("/home/neo/catkin_ws/src/qbo_ai/NEO_EN.brn")
	    else:

		    try:
			    # quickly load binary aiml, fastest way to load all aiml files
			    self.NEO.bootstrap(brainFile = "/home/neo/catkin_ws/src/qbo_ai/NEO_EN.brn")
			    self.brainLoaded = True
		    except:
			    self.forceReload = True

            while True:
                # restart, at each loop, neo.aiml(file containing all new learnt sentences), to instantly add new learnt question to the discussion
                self.NEO.bootstrap(learnFiles="/home/neo/catkin_ws/src/qbo_ai/ai_en/neo.aiml")

                question = raw_input("  Ask me    >>>  ")
                #question = (msg.data)
	        reponse = self.NEO.respond(question)# A commenter pour tester la reco. vocale
	        #reponse = self.NEO.respond(msg.data)# récupère la séquence ententue via qbo_listen et interroge le moteur d'IA
                print "  My answer >>>  "+reponse
                speak_this(reponse)# si une réponse est trouvée, elle est exécutée oralement


    def listen_callback(self, msg):
        print "question = ",msg.data



if __name__ == '__main__':
    try:
        Neo_Chat()
        rospy.spin()
    except rospy.ROSInterruptException: 
        pass
