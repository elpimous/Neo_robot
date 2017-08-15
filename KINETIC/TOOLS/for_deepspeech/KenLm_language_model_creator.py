#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  A simple Kenlm language model creator,
  input your textfile, the context you want for model,
  and compile.
                                Vincent FOUCAULT 2017
"""
import os


os.system('clear')

print('\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print('')
print('                    KENLM Language Model CREATOR')
print('                       Vincent FOUCAULT 2017')
print('')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

"""
/usr/local/bin$ lmplz --text /home/nvidia/deepspeech/DeepSpeech/data/deepspeech_material/train/train_corrected.txt --arpa /home/nvidia/deepspeech/DeepSpeech/data/deepspeech_material/train/train2.arpa --o 5

arpa vers binaire :
-------------------
/usr/local/bin$ ./build_binary -s /home/nvidia/deepspeech/DeepSpeech/data/deepspeech_material/train/train.arpa /home/nvidia/deepspeech/DeepSpeech/data/deepspeech_material/train/train.lm
"""

kenlmDir = ''

def KlmCreator_forArpa():

  while 1:
    textfile =raw_input('\nEnter your textfile dir for the arpa conversion  >>> ')
    confirm2 = raw_input('\n     Your textfile dir is : '+str(textfile)+'. Correct ? y/n   >>> ')
    if confirm2 == str('y'):
        break
    if confirm2 == str('n'):
        print('\nOk, try again...')
        pass

  while 1:
    arpafile =raw_input('\nEnter the arpa file, full path+name  >>> ')
    confirm3 = raw_input('\n     Your textfile dir is : '+str(arpafile)+'. Correct ? y/n   >>> ')
    if confirm3 == str('y'):
        break
    if confirm3 == str('n'):
        print('\nOk, try again...')
        pass

  while 1:
    context =raw_input('\nEnter a value for KenLm --context  >>> ')
    confirm4 = raw_input('\n     The value you choose for --context is : '+str(context)+'. Correct ? y/n   >>> ')
    if confirm4 == str('y'):
        break
    if confirm4 == str('n'):
        print('\nOk, try again...')
        pass

  print('\nProcessing...\n')
  os.system('/home/elpimous/kenlm/build/bin/lmplz --text '+str(textfile)+' --o '+str(context)+' --arpa '+str(arpafile))
  print('\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n°°°')
  print('°°°                    Process DONE. your arpa file should be in : '+str(arpafile))
  print('°°°')
  print('\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n\n     Bye !\n\n\n')


def KlmCreator_forBinary():

  while 1:
    arpaFile =raw_input('\nEnter your arpa dir for the bin conversion  >>> ')
    conf = raw_input('\n     Your arpa dir is : '+str(arpaFile)+'. Correct ? y/n   >>> ')
    if conf == str('y'):
        break
    if conf == str('n'):
        print('\nOk, try again...')
        pass

  while 1:
    binaryFile =raw_input('\nEnter the binary file, full path+name  >>> ')
    conf2 = raw_input('\n     Your binary dir is : '+str(binaryFile)+'. Correct ? y/n   >>> ')
    if conf2 == str('y'):
        break
    if conf2 == str('n'):
        print('\nOk, try again...')
        pass


  print('\nProcessing...\n')
  os.system('/home/elpimous/kenlm/build/bin/./build_binary -s '+str(arpaFile)+' '+str(binaryFile))
  print('\n\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n°°°')
  print('°°°                    Process DONE. your binary file should be in : '+str(binaryFile))
  print('°°°')
  print('\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°\n\n\n')


while 1:
  a = raw_input('\nchoose the process :\n~~~~~~~~~~~~~~~~~~~~~\n\n  1:  to arpa\n  2:  to binary\n\nYour choice ? ')
  if a == str(1):
    KlmCreator_forArpa()
    print('\nBye.\n\n\n')
    break
  if a == str(2):
    KlmCreator_forBinary()
    print('\nBye.\n\n\n')
    break
  else:
    print('wrong choice. please enter 1 or 2 !')
    pass


