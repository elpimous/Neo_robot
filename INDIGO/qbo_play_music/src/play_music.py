#!/usr/bin/env python
# -*- coding: utf-8 -*-


#********************************************************************
#
#
#           A SIMPLE MEDIA PLAYER CONTROLLED BY VOICE
#
#                READ TEXT FILE FOR DEPENDENCIES
#
#             ANSWER SPOKEN WITH QBO_TALK (PICO2WAVE)
#
#                     elpimous12@orange.fr
#
#
#********************************************************************

import rospy,roslib
import os,random
import subprocess
import time
from syscall import runCmd
from random import choice
from qbo_talk.srv import Text2Speach
from std_msgs.msg import String
#from lib_qbo_pyarduqbo import qbo_control_client
#from qbo_arduqbo.msg import Nose # nose colors

def run_process(command = ""):
    if command != "":
        return subprocess.Popen(command.split())
    else:
        return -1

class mediaPlayer():

  def __init__(self):

        rospy.init_node('qbo_play_music')
        #self.qbo_controller=qbo_control_client()
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
        self.detected = True
        self.en_attente_ordres = False
        #self.nose_pub = rospy.Publisher('/cmd_nose', Nose, queue_size=10) # nose color
        rospy.Subscriber('listened', String, self.Choice)
	self.pkg_dir = roslib.packages.get_pkg_dir("qbo_play_music")
        self.dir = self.pkg_dir+"/audios/"
        self.count = len([f for f in os.listdir(self.dir) if os.path.isfile(os.path.join(self.dir, f))])
        self.song_info = ""
        self.started = False
        self.waitingForOrders = False
        self.secs = int(0)
        self.pause = False
        #self.no_nose = False
        #self.green_nose = False
        print "clear xmms2"
        runCmd("xmms2 clear") # clear xmms2_server 
        print "Add song to xmms2 server"
        runCmd("xmms2 add "+self.pkg_dir+"/audios/") # add all musics in xmms2_server
        self.speak_this("Les musiques sont prêtes, prononce le mot - Lecture - quand tu es prêt,")
        print "Ready !"


  def speak_this(self,text):
	self.client_speak(str(text))

  def get_song_info_2(self): # return name of actual music
    (ph_out, ph_err, ph_ret) = runCmd("nyxmms2 list")
    out_str = str(ph_out)
    self.song_info = out_str.split("->")
    self.song_info = self.song_info[1]
    self.song_info = self.song_info.split("]")
    self.song_info = self.song_info[1]
    self.song_info = self.song_info.split("(")
    self.song_info = self.song_info[0]
    self.song_info = self.song_info.split(".")
    self.song_info = self.song_info[0]
    self.song_info = self.song_info.strip()
    self.song_info = self.song_info.split(" - ")
    return self.song_info


  def Choice(self, msg):
      if self.waitingForOrders == True :# and not self.started :
        self.sentence = msg.data
        # how many titles
	if self.sentence.find("combien") > -1 :
          howManyTiltes = ["Attends, Je regardes. Il y a "+str(self.count)+" musiques dans mon dossier","Dans mon disque, j'ai "+str(self.count)+" musiques disponibles. C'est pas beaucoup, mais elles sont super.",str(self.count)+". J'ai "+str(self.count)+" titres dans ma mémoire"]
          self.speak_this(choice(howManyTiltes))
          self.pause = False

        # Title name
	if self.sentence.find("nom") > -1 or self.sentence.find("titre") > -1 :
          print " - TITRE DE MUSIQUE DEMANDE,"
          self.get_song_info_2()
          self.speak_this("Titre en cours, "+self.song_info[0].replace("_"," "))
          self.sentence = "blabla"
          self.pause = False

        # Previous
	if self.sentence.find("précédent") > -1 or self.sentence.find("précédente") > -1 :
          print " - MUSIQUE PRECEDENTE DEMANDEE,"
          runCmd("xmms2 prev") # play server
          self.sentence = "blabla"
          self.speak_this("D'accord, je sélectionne la musique précédente")
          self.pause = False

        # Next
	if self.sentence.find("suivant") > -1 or self.sentence.find("suivante") > -1 :
          print " - MUSIQUE SUIVANTE DEMANDEE,"
          runCmd("xmms2 next") # play server
          self.sentence = "blabla"
          self.speak_this("D'accord, je sélectione la musique suivante")
          self.pause = False

        # stop
	if self.sentence.find("stop") > -1 :
          print " - ARRET DEMANDE."
          runCmd("xmms2 stop") # play server
          self.sentence = "blabla"
          time.sleep(1)
          self.speak_this("D'accord, A +,")
          run_process("rosnode kill /qbo_play_music")
          run_process("rosnode kill /qbo_listen")

        # Play
	if self.sentence.find("lecture") > -1 :
          print " - LECTURE DEMANDEE,"
          self.get_song_info_2()
          #self.speak_this("Bien, je lis la musique, "+self.song_info[0].replace("_"," "))
          self.pause = False
          runCmd("amixer -c 1 sset Mic,1 0%")
          runCmd("amixer -c 1 sset Mic,0 0%")
          self.speak_this("Je démarre la lecture,")
          runCmd("xmms2 play") # play server
          self.started = True
      else : pass 


  def main(self):

    rate = rospy.Rate(2) # 1s
    while not rospy.is_shutdown(): # loop each second
      #nose_command=Nose()
      self.waitingForOrders = False

      if self.Detected :
          self.waitingForOrders = True
          print "detected !"
          """
          if not self.green_nose : 
            nose_command=Nose()
            nose_command.color = 2
            self.sec = rospy.get_rostime()
            self.secs = now.secs
            self.green_nose = True
            self.no_nose = False
            self.nose_pub.publish(nose_command)
          #self.started = False
          self.sentence = "blabla"
          """
          if self.pause == False :
            runCmd("xmms2 pause") # play server
            runCmd("amixer -c 1 sset Mic,1 75%")
            #runCmd("amixer -c 1 sset Mic,0 75%")
            print " En attente d'ordres..."
            self.pause = True

      #if self.waitingForOrders == False :
        #if not self.no_nose : 
          #nose_command.color = 0
          #self.nose_pub.publish(nose_command)
          #self.green_nose = False
          #self.no_nose = True

      # time delay 4 sec
      if not self.waitingForOrders and self.started and self.pause :
        if (now.secs - self.secs) == int(5) :
          # pause finished, I play
          print " ca fait 4 secondes"
          self.pause = False
          runCmd("amixer -c 1 sset Mic,1 0%")
          runCmd("amixer -c 1 sset Mic,0 0%")
          self.speak_this("Je reprends la lecture,")
          runCmd("xmms2 play") # play server
          self.started = True

      rate.sleep()

if __name__ == '__main__':
    try:
        mediaPlayer = mediaPlayer().main()
        rospy.spin()
    except rospy.ROSInterruptException: pass
