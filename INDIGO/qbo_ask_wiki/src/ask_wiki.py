#!/usr/bin/env python
# -*- coding: utf-8 -*-


######################################################################################################
#                                                                                                    #
#                       A NODE TO LET ROBOT SPEAK WIKIPEDIA REQUESTS                                 #
#                     THIS PROGRAM OPENS A SERVICE AND WAIT FOR REQUEST                              #
#                        wHEN REQUEST DONE, OR ERROR, ROBOT SPEAKS                                   #
#                                                                                                    #
#               Vincent FOUCAULT       elpimous12@orange.fr            8 MAY 2016                    #
######################################################################################################


import rospy # for ROS
import random
import wikipedia # for wikipedia internet requests
from random import choice
from qbo_talk.srv import Text2Speach # for robot voice
from qbo_ask_wiki.srv import ask # read service content (words we want to be searched)


class search():


    def __init__(self):

        rospy.init_node('qbo_wiki', anonymous=True)
        fr1 = rospy.Service('/wiki', ask, self.ask)
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
	wikipedia.set_lang("fr") # request language



    def speak_this(self,text): # robot voice
        self.client_speak(str(text))



    def ask(self, word): 
        self.Sentence = ""
        wordSearch = word.sentence
        try:
        	search = wikipedia.summary(wordSearch, sentences=3)
        except :
		pass
        try:
        	self.Sentence = search.replace('(','').replace(')','') # remove parenthesis from text for better speaking
        except :
		pass
        try:
        	a = self.Sentence.split('[')[0] # remove phonetics
        	b = self.Sentence.split(']')[1]
        	self.Sentence = a+b 
        except :
		pass
        try:
                if self.Sentence == "":
                        samples = ["Essaie d'être plus précis","Je n'ai mas trouvé"]
			self.speak_this(random.choice(samples)) # not found or too much choices, robot alerts us !

	        text = (self.Sentence).encode('utf-8')
                self.speak_this(text) # robot speaks wiki content if found !
        except :
		pass


if __name__ == '__main__':

  try:
    node = search()
    rospy.spin()

  except rospy.ROSInterruptException:
    print "Leaving qbo_wiki node"
    
    
