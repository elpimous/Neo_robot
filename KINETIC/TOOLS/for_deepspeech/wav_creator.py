#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" simple python program who creates wavfiles, regardint to a text containing sentences to speak
    elpimous12 @2017 (for deepspeech deep learning project.)
"""

import os
import pyaudio
import wave


os.system('clear')

# text containing sentences
#text_link = raw_input("\n  >> Ou se trouve le fichier texte à lire ?? : ")
text_link = '/home/nvidia/Documents/voices/sentences2.txt'
text = open(text_link)
textfile = text.readlines()

print('\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print('°°                                                                                    °°')
print('°°                         séquences à lire : '+str(len(textfile))+' lignes')
print('°°                                                                                    °°')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

print('°°                                   PRET A ENREGISTRER                               °°')
print('°°°°°°°°°°°°°°°°°°°°°°°                                      °°°°°°°°°°°°°°°°°°°°°°°°°°°')
raw_input('\n\nappuyer sur "entrée" pour continuer')

cont = int(raw_input("\n\n  >> quel est l'index du dernier enregistrement effectue ? : "))
cont2 = int(raw_input("\n\n  >> quel est la ligne du texte à lire ? : "))
cont2-=1
conttext = 0
location = '/home/nvidia/Documents/voices/record.'

os.system('clear')

def read(data):
	index = data
	print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
	print(' Lire à haute voix :  '+str(textfile[index]))
	print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

	return
	
def record(data):
	index = data
	threshold = '0.1%'
	end_threshold = '0%'
	os.system('sox -c 1 -r 16000 -t alsa default '+index+'.wav silence 1 0.1 '+threshold+' 1 1.5 '+end_threshold)
	print('\n                  saved to : '+str(index)+'.wav')
	return
	
def clear():
    os.system('clear')
    
def recording_process():
    a=(len(textfile))
    #for value in range(cont,(a)):
    for value in range(cont,(a)):
        read((value-cont)+cont2)
        record(location+str(value+1))
        while True:
            keyboard = raw_input('\n                           GARDER : "enter",     RECOMMENCER : "r" \
                              \n                           ========              ============= \
                              \n                                       >>> ')
            if keyboard == '':
                clear()
                break
            if keyboard == 'r':
                print('\n\n              Nouvel essai\n')
                read((value-cont)+149)
                record(location+str(value+1))
                clear()
            else:
                print('\nVeuillez entrer une touche référencée ci-dessus !!')
                clear()


    
if __name__ == "__main__":
       clear()
       start = recording_process()
