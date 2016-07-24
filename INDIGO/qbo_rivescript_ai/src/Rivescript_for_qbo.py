#!/usr/bin/python2
# -*- coding: utf-8 -*-

import re
import rospy
from rivescript import RiveScript
from qbo_talk.srv import Text2Speach
from std_msgs.msg import String


def speak_this(text): # for qbo_talk
    global client_speak
    client_speak(str(text))


class RS_AI():

	def __init__(self):

		rospy.init_node( 'qbo_rivescript_ai', anonymous=True )
		self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
		rospy.Subscriber('listened', String, self.listen_callback)
		self.ai = RiveScript(utf8=True)
		self.ai.unicode_punctuation = re.compile(r'[.,!?;:]')
		self.ai.load_directory("/home/neo/catkin_ws/src/qbo_rivescript_ai/src/eg/neo_brain")
		self.ai.sort_replies()


	def speak_this(self,text):
		self.client_speak(str(text))

	def listen_callback(self,msg):
		sentence = msg.data
		if sentence != "rienrien" :
			print ("user --> ", sentence, "\n")
			if sentence.find('je veux quitter')>-1 or sentence.find('je souhaite quitter')>-1:
				self.speak_this('ok, a+')
				quit()
			reply = self.ai.reply("localuser", sentence)
			print ("Neo --> ", reply, "\n")
			replyUTF = reply.encode('utf8')
			self.speak_this(replyUTF)
			sentence = "rienrien"

		else :
			pass

if __name__ == "__main__":
    try:
       RS_AI()
       rospy.spin()
    except rospy.ROSInterruptException: 
       rospy.loginfo ("Exiting program")
    pass

