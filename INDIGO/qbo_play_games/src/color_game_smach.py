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
import smach
import smach_ros
import math
import sys
import random
from threading import Thread
from random import choice
from time import sleep
from std_msgs.msg import String
from qbo_talk.srv import Text2Speach


class Game(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["neo_turn"])
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)

    def speak_this(self,text): # robot voice
        self.client_speak(str(text))

    def execute(self, userdata):
	intro = ('Super, Allonzy pour le jeu des couleurs,','Ok, prépare les balles-de-couleur,')
	self.speak_this(random.choice(intro))
	self.speak_this("Montre-moi-une-balle et j'essairai de trouvé-sa couleur.")
        # this random choose who will start
        return 'neo_turn'




class Alternate(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=['neo_turn','human_turn'])
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
        rospy.Subscriber('/listened', String, self.listen_callback, queue_size = 5)
        rospy.Subscriber('/ball_color', String, self.Color)

    def speak_this(self,text): # robot voice
        self.client_speak(str(text))

    def listen_callback(self,msg): # for qbo_listen
        self.heard = msg.data
        print "***** "+self.heard+" *****"

    def Color(self,msg): # for qbo_listen
        self.ballColor = msg.data

    def execute(self, userdata):
        sleep(0.4)
        turn = random.choice([1, 2])
        if turn == 1:
            return 'neo_turn'
        if turn == 2:
            return 'human_turn'




class neo_turn(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["alternate"])
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
        rospy.Subscriber('/ball_color', String, self.Color)
        self.alreadyStarted = False
        self.alreadySpoken = False

    def speak_this(self,text): # robot voice
        self.client_speak(str(text))

    def Color(self,msg): # for qbo_listen
        self.ballColor = msg.data

    def execute(self, userdata):
       	color_choice = 	(
			#'rouge',
			'verte',
			#'bleue'
			)
        self.randColor = (random.choice(color_choice))

        if not self.alreadyStarted:
        	self.speak_this("Tu es prêt ? Je commence,")

        # Question
	choice1 = 	(
			'Montres moi la boule '+self.randColor+',',
			'fais voir la boule '+self.randColor+',',
			'Ou est la boule '+self.randColor+','
			)

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


        # Response
        if self.ballColor == "no_color":
                waiting = ("Bon, j'attends,","sait-quand tu veux,","Allez,")
                #sleep(2)
                self.speak_this(random.choice(waiting))

        while not rospy.is_shutdown():


            if self.ballColor != "no_color":

                if self.ballColor != str(self.randColor):
                    color = 	(
				"Non, mauvaise couleur. Essaye encore,",
				"Surement pas. C'est une balle "+self.ballColor,
				"Tu me montre une balle "+self.ballColor+", et je t'ai demandé une balle "+str(self.randColor),
				"Non, ce n'est pas une boule "+str(self.randColor)
				)
		    self.speak_this(random.choice(color))

                if self.ballColor == str(self.randColor):
                    color = 	(   
				"Je vois bien la balle"+str(self.randColor), 
				"Oui, c'est bien une boule "+str(self.randColor),
				"Une boule "+str(self.randColor)+", Parfait,"
			    	)
		    self.speak_this(random.choice(color))
                    self.alreadyStarted = True
                    return 'alternate'




class human_turn(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["alternate"])
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
        rospy.Subscriber('/listened', String, self.listen_callback, queue_size = 5)
        rospy.Subscriber('/ball_color', String, self.Color)

    def speak_this(self,text): # robot voice
        self.client_speak(str(text))

    def listen_callback(self,msg): # for qbo_listen
        self.heard = msg.data
        print "***** "+self.heard+" *****"

    def Color(self,msg): # for qbo_listen
        self.ballColor = msg.data

    def execute(self, userdata): # c'est déja un loop
          neoColorThinking = 	(
				"A ton tour. Montre moi une balle,",
				#"C'est à moi de trouver la couleur. Fais voir la balle,",
				#"A moi. Où est la balle ?"
				)
          self.speak_this(random.choice(neoColorThinking))


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
			pass

                if self.heard.find("néo je souhaite quitter") > -1 or self.heard.find("néo je veux quitter") > -1:
                        self.speak_this("C'était sympas d'avoir joué avec moi,")
                        sleep(0.2)
			sys.exit

                if self.heard.find("oui") > -1:
                        good = ("Super,","Bien,","Trop bien,","Ok,")
              		self.speak_this(random.choice(good))
                        return 'alternate'

          else :
                pass

def main():
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['exit'])
    with sm:
        smach.StateMachine.add('GAME', Game(), transitions={'neo_turn':'NEO_TURN'})
        smach.StateMachine.add('NEO_TURN', neo_turn(), transitions={'alternate':'ALTERNATE'})
        smach.StateMachine.add('HUMAN_TURN', human_turn(), transitions={'alternate':'ALTERNATE'})
        smach.StateMachine.add('ALTERNATE', Alternate(), transitions={'neo_turn':'NEO_TURN','human_turn':'HUMAN_TURN'})
    sis= smach_ros.IntrospectionServer('server_name',sm,'/color_balls')
    sis.start()

    # Execute SMACH plan
    rospy.loginfo("color_balls launched")
    outcome = sm.execute()
    rospy.loginfo('color_balls Finished')
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    try:
        rospy.init_node("qbo_play_color_balls")
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo("color_balls node terminated.")










