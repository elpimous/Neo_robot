QBO_TALK
========

#   This is a Espeak wrapper for QBO robot from THE CORPORA          #
#   It uses Mbrola to produce nice voice.                            #
#   Actually it's in French, and English  but it's easy to change :  #
#                                                                    #
######################################################################


Open a terminal :

*****************************
sudo apt-get install espeak
sudo apt-get install mbrola
***************************************************************************************************************
download your mbrola voices, (here, download al least Fr1 and En1. Those voices are quite better than festival
Voices can be directly downloaded on ubuntu 14.04 software downloads
***************************************************************************************************************


this node creates a service called "/say_(chosen language)"


*** When qbo_talk is running, you can make QBO speak with this: ***

open one terminal : rosrun qbo_talk neo_talk.py

in other terminal : rosservice call /say_fr1 "salut tout le monde"
                    rosservice call /say_en1 "hello world"

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

NEW :

	A MODIFICATION FOR ASUS XTION MICS (QUITE BETTER THAN QBO ONES)
        BE SURE TO HAVE PRIMESENSE MIC WORKING (TEST IT ON AUDACITY, you'll see an enormous difference !!!)
	
	no need qbo_audio_control.
	faster ! nearly 1.5 seconds per process, and a clear recording

        When you speak a sentence, xtion mic mute
	when finished speaking, xtion mic unmute

	***   neo_talk_to_xtion_mic.py   ***

++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

SOON :

	an alternative to ESPEAK / MBROLA.

        SVOX PICO use in qbo_talk

	quality between mbrola and acapela (french, dutch, english, spanish, and perhaps more...)


