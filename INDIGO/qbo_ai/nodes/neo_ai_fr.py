#!/usr/bin/env python
# -*- coding: utf-8 -*-


#********************************************************************
#
#
#        ARTIFICIAL INTELLIGENCY WITH PY-AIML (ALICE STYLE)
#
#                 KEYBOARD INPUTS FOR QUESTIONS
#
#                   ANSWER SPOKEN WITH ESPEAK
#
#                    elpimous12@orange.fr
#
#
#********************************************************************

"""
	For english :
		- l41 (/say_en1)
		- l63 (ai_en)

"""

import rospy
from qbo_talk.srv import Text2Speach
from std_msgs.msg import String
import aiml_fr
import sys

def speak_this(text): # for qbo_talk
    global client_speak
    client_speak(str(text))

class Neo_Chat():

    def __init__(self):
	global client_speak
        client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
        rospy.init_node('neo_chat_node', anonymous=True)
        self.NEO = aiml_fr.Kernel()# charge le moteur de l'IA
        self.brainLoaded = False # False to reload all aiml files !!!
        self.forceReload = True # force reload of all aiml files
	# Données personnelles du robot, comme son nom, ses préférences...
        self.NEO.setBotPredicate('name', "Naio")
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
		    self.NEO.bootstrap(learnFiles="/home/neo/catkin_ws/src/qbo_ai/neo_ai.fr/*.aiml")# charge tous les fichiers aiml
		    self.brainLoaded = True


		    # backup des differents fichiers aiml dans un fichier compressé, pour un chargement éclair les fois suivantes
		    self.NEO.saveBrain("/home/neo/catkin_ws/src/qbo_ai/NEO.brn")
	    else:

		    try:
			    # chargement rapide des fichiers aiml, si existance du fichier compressé
			    self.NEO.bootstrap(brainFile = "/home/neo/catkin_ws/src/qbo_ai/NEO.brn")
			    self.brainLoaded = True
		    except:
			    self.forceReload = True

            while True:
                question = raw_input("posez votre question : ")
                #question = (msg.data)
	        reponse = self.NEO.respond(question)# A commenter pour tester la reco. vocale
	        #reponse = self.NEO.respond(msg.data)# récupère la séquence ententue via qbo_listen et interroge le moteur d'IA
                print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n"
                print "  réponse : ",reponse
                print "\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n"
                speak_this(reponse)# si une réponse est trouvée, elle est exécutée oralement


if __name__ == '__main__':
    try:
        Neo_Chat()
        rospy.spin()
    except rospy.ROSInterruptException: 
        pass
