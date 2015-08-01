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






NEW  : May 29, 2015

***************************************************************************************************************

Actually, qbo_talk configured to work with SVOX (quite better voice, between mbrola and acapela voices)

********************************************
sudo apt-get install libttspico-utils
********************************************
To test, execute :

$ pico2wave -w /tmp/test.wav "Hello World"  #record sentence in spoken wav file
$ aplay /tmp/test.wav                       # play sentence
********************************************

