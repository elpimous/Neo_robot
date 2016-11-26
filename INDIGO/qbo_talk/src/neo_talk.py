#!/usr/bin/env python
# coding: utf-8


# Author: Vincent FOUCAULT
# Here is a text-to-speech using svoxpico


import rospy
import roslib
from qbo_talk.srv import Text2Speach # read service content (words we want to be spoken)
import os
from time import sleep

# Some possibilities of different languages

#--- espeak
#fr1_speak = "espeak -a 70 -s 140 -p50 -v mb/mb-fr1 \"%s\" | mbrola -e -C \"n n2\" /usr/share/mbrola/voices/fr1 - -.au | paplay"
#en1_speak = "espeak -a 70 -s 140 -p50 -v mb/mb-en1 \"%s\" | mbrola -e -C \"n n2\" /usr/share/mbrola/voices/en1 - -.au | paplay"

#--- padsp (for some specific providers)
#fr1_speak = "padsp swift \"%s\""

#--- pico2wave
fr1_speak = "pico2wave -l fr-FR -w test.wav \"%s\" && play test.wav"
en1_speak = "pico2wave -l en-GB -w test.wav \"%s\" && play test.wav"
      

class talk():

    def __init__(self):

        rospy.init_node('talk', anonymous=True)
        fr1 = rospy.Service('say_fr1', Text2Speach, self.fr1_talk)
        #en1 = rospy.Service('say_en1', Text2Speach, self.en1_talk)
        

    #TODO  Dic. words fo gain better words sounds ! 

    def fr1_talk(self, speak): 
      try :
        # open talk_dic_fr to read words inside
        pkg_dir = roslib.packages.get_pkg_dir("qbo_talk")
 
        # FR #
        with open(pkg_dir+"/params/talk_dic_fr","r") as dic:
        # EN #
        #with open(pkg_dir+"/params/talk_dic_en","r") as dic:

          self.dico = dic.read()
          dico = self.dico.split("\n")

          self.Cut_mics()

          # replace word with modified one in dic, for better sound
          New = speak.sentence.split(" ")
          for w in New :
           for i in dico :
            if i.find(w) == 0 :
              a = i.split(" > ")
              speak.sentence = speak.sentence.replace(w, a[1])
           continue
        dic.close()
        print "good"
        self.Cut_mics()
        os.system(fr1_speak % str(speak.sentence))
        self.Open_mics()
        return True


      except :
      	  print "exception"
      	  self.Cut_mics()
          os.system(fr1_speak % str(speak.sentence))
          self.Open_mics()
          return True

    """
    def en1_talk(self, speak):
        os.system(en1_speak % speak.sentence)
        return []
    """

    def Cut_mics(self):
          # When speaking, micros cut (0 %)  /OFF
          os.system("amixer -c 1 sset Mic,0 nocap")
          os.system("amixer -c 1 sset Mic,1 nocap")
          sleep (0.1)

    def Open_mics(self):
          # When finished speaking, micros hear again (70 %)  /ON
          #sleep (0.1)
     	  os.system("amixer -c 1 sset Mic,0 cap")
          os.system("amixer -c 1 sset Mic,0 70%")


if __name__ == '__main__':
    try:
        talk = talk()
        rospy.spin()
    except rospy.ROSInterruptException: pass


