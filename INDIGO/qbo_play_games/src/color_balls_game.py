#!/usr/bin/env python
# -*- coding: utf-8 -*-

######################################################################
#
#  Color_game,
#
#  Robot asks for a ball color, between Red / Green / yellow / Blue
#  It tracks object, sees color, and send answer,
#  - if correct, it asks for a next color,
#  - else, it send incorrect color and asks again for needed color
#  after some time, it proposes to stop game
#
#  I used threading process, to improve speed.
#
#
#  need to fix HSV use (wrong conversion colors ?!!!)
#
#                   Vincent FOUCAULT 6 APRIL 2016
######################################################################

import rospy
import math
import sys
import subprocess
import random
from threading import Thread
from random import choice
from time import sleep
from std_msgs.msg import String
from qbo_talk.srv import Text2Speach


class Game():

    def __init__(self):
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
        rospy.Subscriber('/listened', String, self.listen_callback, queue_size = 5)
        rospy.Subscriber('/ball_color', String, self.Color)
        #rospy.on_shutdown(self.exiting)
        self.alreadySpoken = False
        self.heard = ""

    def run_process(self, command = ""):
        if command != "":
            return subprocess.Popen(command.split())
        else:
            return -1

    def speak_this(self,text):
        self.client_speak(str(text))

    def listen_callback(self,msg):
        self.heard = msg.data
        # Exit
        if self.heard.find("je veux quitter") > -1 or self.heard.find("je souhaite quitter") > -1:
            sleep(1)
            self.speak_this("Ok, Merci d'avoir joué avec moi, c'était coul,")
            self.exiting()

    def Color(self,msg):
        self.ballColor = msg.data


    def start(self):
        #self.speak_this("Salut-laizamis. Aujourd'hui, je vous présente mon nouveau jeu. un jeu basé sur les couleurs et l'échange.")
	intro = ('Allonzy pour le jeu des couleurs,','prépare les bal-de-couleur,')
	self.speak_this(random.choice(intro))
	self.speak_this("Je t'explique les règles : soit je te demande une couleur et tu dois me montrer la bonne bal, soit tu me montre la bal et tu me demande la couleur. J'essairai de te répondre.")
        self.speak_this("Et si tu veux sortir du jeu, tu n'as qu'a dire que tu veux ou tu souhaite quitter le jeu ou la partie,")
        self.speak_this("Tu es prêt ?")

        self.neo_turn()

    """
    def alternate(self):
        print "alternate !"
        sleep(0.2)
        turn = random.choice([1, 2])
        if turn == 1:
            print "choix 1"
            self.neo_turn()
        if turn == 2:
            print "choix 2"
            self.human_turn()
    """


    def neo_turn(self):

        exit_loop = False
        print "neo_turn !"
       	color_choice = 	(
			'rouge',
			'verte',
			'bleue'
			)
        self.randColor = (random.choice(color_choice))

        # Question
	choice1 = 	(
			'Montres moi la boule '+self.randColor+',',
			'fais voir la boule '+self.randColor+',',
			#'Ou est la boule '+self.randColor+','
			)

        """
	choice2 = 	(
			"Et maintenant, la "+self.randColor+",",
			"Au tour de la boule "+self.randColor+","
			)

        if not self.alreadySpoken:
            	self.speak_this(random.choice(choice1))
                self.alreadySpoken = True
        else :
                a = random.choice([1, 2])
                if a == 1:
                    self.speak_this(random.choice(choice1))
                else:
                    self.speak_this(random.choice(choice2))
        """
        self.speak_this("A moi.")
        self.speak_this(random.choice(choice1))

        """
        # Response
        if self.ballColor == "no_color":
                #waiting = ("Bon, j'attends,","sait-quand tu veux,","Allez,")
                #sleep(2)
                self.speak_this(random.choice(waiting))
        """

        while not exit_loop:

            if self.ballColor != "no_color":

                if self.ballColor != str(self.randColor):
                    color = 	(
				"Non, mauvaise couleur. Essaye encore,",
				"Surement pas. C'est une balle "+self.ballColor+", recommence,",
				"Tu me montre une balle "+self.ballColor+", et je t'ai demandé une balle "+str(self.randColor)+", recommence,",
				"Non, ce n'est pas une boule "+str(self.randColor)+", recommence,"
				)
		    self.speak_this(random.choice(color))

                if self.ballColor == str(self.randColor):
                    color = 	(   
				"Je vois bien la balle"+str(self.randColor), 
				"Oui, c'est bien une boule "+str(self.randColor),
				"Une boule "+str(self.randColor)+", Parfait,"
			    	)
		    self.speak_this(random.choice(color))
                    exit_loop = True

            else:
		pass

        #self.alternate()
        self.human_turn()


    def human_turn(self):

        exit_loop = False
        print "human_turn !"
        neoColorThinking = 	(
				"A mon tour. Montre-moi une balle,",
				"C'est à moi de trouver la couleur. Fais voir la balle,",
				"A moi. Où est la balle ?"
				)
        self.speak_this(random.choice(neoColorThinking))

        while not exit_loop:

          if self.ballColor != "no_color":

            if self.heard.find("couleur") > -1:

                if self.ballColor == "no_color":
		    self.speak_this("Je ne vois pas bien la balle !")
                    #continue

                neoColorThinking = 	(
					"Je pense que cette balle est "+self.ballColor,
					"Il me semble qu'elle est "+self.ballColor,
					self.ballColor+" la balle est "+self.ballColor,
					"cette balle est "+self.ballColor
					)
		self.speak_this(random.choice(neoColorThinking))

                doYouAgree =		(
					"C'est ça ?",
					"J'ai bon ?",
					)
		self.speak_this(random.choice(doYouAgree))

                # probleme de boucle!!

                rospy.wait_for_message('/listened', String)

                if self.heard.find("non") > -1:
                        bad = ("zute","Bon,","Ah, mince,","Ok,")
              		self.speak_this(random.choice(bad))
              		self.speak_this("remontre la balle,")
			continue

                if self.heard.find("oui") > -1:
                        good = ("Super,","Bien,","Trop bien,","Ok,")
              		self.speak_this(random.choice(good))
                        exit_loop = True
        #self.alternate()
        self.neo_turn()

    def exiting(self):
        print "\nLeaving game"

        self.run_process("rosnode kill /qbo_color_balls_publisher")
        self.run_process("rosnode kill /qbo_listen")
        sleep(0.2)
        self.run_process("rosnode kill /qbo_color_balls_game")
        self.speak_this("Je quitte,")

if __name__ == '__main__':
    #try:
        rospy.init_node("qbo_play_color_balls")
        a = Game()
        b = a.start()
    #except rospy.ROSInterruptException:
        #rospy.loginfo("color_balls node terminated.")
















