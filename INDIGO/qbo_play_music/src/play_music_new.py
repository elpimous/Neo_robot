#!/usr/bin/env python
# -*- coding: utf-8 -*-

#********************************************************************
#
#           A SIMPLE MEDIA PLAYER CONTROLLED BY VOICE
#                READ TEXT FILE FOR DEPENDENCIES
#
#             ANSWER SPOKEN WITH QBO_TALK (PICO2WAVE)
#
#           ** Pause music, just with gently head movement 
#                     by humain interaction **
#
#                     elpimous12@orange.fr
#
#                  version 1.02 (23 avril 2016)
#
#********************************************************************

import rospy,roslib
import os,random
import subprocess
from time import sleep
from syscall import runCmd
from random import choice
from qbo_talk.srv import Text2Speach
from std_msgs.msg import String

def run_process(command = ""):
    if command != "":
        return subprocess.Popen(command.split())
    else:
        return -1

class mediaPlayer():

  def __init__(self):

        rospy.init_node('qbo_play_music')
        rospy.on_shutdown(self.exit)
        self.client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach)
        self.en_attente_ordres = False
        rospy.Subscriber('listened', String, self.Choice)
        rospy.Subscriber('/head_joy', String, self.pause_detector)
        self.pkg_dir = roslib.packages.get_pkg_dir("qbo_play_music")
        self.dir = self.pkg_dir+"/audios/"
        self.count = len([f for f in os.listdir(self.dir) if os.path.isfile(os.path.join(self.dir, f))])
        self.song_info = ""
        self.started = False
        self.Detected = False
        self.waitingForOrders = True
        self.ok_I_pause = ""
        self.sentence = ""
        self.secs = int(0)
        self.pause = False
        print "clear xmms2"
        runCmd("xmms2 clear") # clear xmms2_server 
        print "Add song to xmms2 server"
        runCmd("xmms2 add "+self.pkg_dir+"/audios/") # add all musics in xmms2_server

  def speak_this(self,text):
	self.client_speak(str(text))

  def get_song_info_2(self): # return name of actual music
   try:
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
   except :
    return "titre inconnu"

  def pause_detector(self, msg):
      self.ok_I_pause = msg.data

  def Cut_mics(self):
          runCmd("amixer -c 1 sset Mic,0 nocap")
          sleep(0.1)

  def Open_mics(self):
          sleep(0.1)
          runCmd("amixer -c 1 sset Mic,0 cap")

  def Choice(self, msg):
      if self.waitingForOrders == True :# and not self.started :
        self.sentence = str(msg.data)
        # how many titles
	if self.sentence == str("combien"):
          howManyTiltes = ["Attends, Je regardes. Il y a "+str(self.count)+" musiques dans mon dossier","Dans mon disque, j'ai "+str(self.count)+" musiques disponibles. C'est pas beaucoup, mais elles sont super.",str(self.count)+". J'ai "+str(self.count)+" titres dans ma mémoire"]
          print "- NOMBRE DE MUSIQUES DEMANDE,"
          self.speak_this(choice(howManyTiltes))
          self.pause = False

        #TODO travailler sur les titres des zic (23 avril 2016)
        """
        # Title name
	if self.sentence.find("nom") > -1 or self.sentence.find("titre") > -1 :
          print " - TITRE DE MUSIQUE DEMANDE,"
          self.get_song_info_2()
          self.speak_this("Titre en cours, "+self.song_info[0].replace("_"," "))
          self.sentence = "blabla"
          self.pause = False
        """

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
	if self.sentence.find("stop la musique") > -1 :
          print " - ARRET DEMANDE."
          runCmd("xmms2 stop") # play server
          self.sentence = "blabla"
          sleep(0.1)
          self.speak_this("D'accord, A +,")
          run_process("rosnode kill /qbo_play_music")
          run_process("rosnode kill /qbo_listen")

        # Play
	if self.sentence.find("lecture") > -1 :
          print " - LECTURE DEMANDEE,"
          self.get_song_info_2()
          #self.speak_this("Bien, je lis la musique, ")#+self.song_info[0].replace("_"," "))
          self.pause = False
          self.speak_this("Je démarre la lecture,")
          self.Cut_mics()
          runCmd("xmms2 play") # play server
          self.started = True
      else : pass 


  def main(self):
    self.speak_this("Les musiques sont chargées. Prononce le mot - Lecture, - quand tu es prêt,")

    while not rospy.is_shutdown(): # loop each second
      # PAUSE WITH HAND
      #self.waitingForOrders = False
      rospy.wait_for_message('/head_joy', String, timeout=None)
      if self.ok_I_pause == "left" or self.ok_I_pause == "right":
          self.waitingForOrders = True
          self.Open_mics()
          print "pause needed"
          #self.started = False
          self.sentence = "blabla"
          if self.pause == False :
            runCmd("xmms2 pause") # play server
            self.speak_this("Oui?")
            sleep(0.1)
            print " En attente d'ordres..."
            self.pause = True

      # time delay 4 sec
      if not self.waitingForOrders and self.started and self.pause :
        if (now.secs - self.secs) == int(5) :
          # pause finished, I play
          print " ca fait 4 secondes"
          self.pause = False
          self.speak_this("Je reprends la lecture,")
          self.Cut_mics()
          runCmd("xmms2 play") # play server
          self.started = True

  def exit(self):
	runCmd("xmms2 clear")
        sleep(0.1)
	runCmd("xmms2 exit")
        sleep(0.1)
        run_process("rosnode kill /qbo_head_joy")
    

if __name__ == '__main__':
    try:
        mediaPlayer = mediaPlayer().main()
        #rospy.spin()
    except rospy.ROSInterruptException: pass
