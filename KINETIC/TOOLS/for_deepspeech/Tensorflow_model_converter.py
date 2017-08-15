#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
  A simple converter for the Tensorflow modele.
  can convert a .pbtxt file to a .pb binary one
                          Vincent FOUCAULT 2017
"""
import os
print('Wait for Tensorflow ...')
import tensorflow as tf
from google.protobuf import text_format
from tensorflow.python.platform import gfile

os.system('clear')

print('\n°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')
print('')
print('           TENSORFLOW .pbtxt from/to .pb   CONVERTER')
print('                               Vincent FOUCAULT 2017')
print('')
print('°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°°')

def pbtxt2pb():

  while 1:
    filename = raw_input('\nenter your complete .pbtxt file link\n  >>  ')
    try:
      link = open(filename, 'r')
      graph_def = tf.GraphDef()
      print('\nreading the pbtxt file')
      file_content = link.read()
      text_format.Merge(file_content, graph_def)
      tf.import_graph_def(graph_def, name='')
      print('\nreading file DONE !')
      break
    except :
      print('\nplease, verify that the .pbtxt link is correct !')
    
  while 1:
    filename2 = raw_input('\n\nenter the .pb destination file link\n  >>  ')
    try:
      print('\nwriting the bp file\n')
      tf.train.write_graph(graph_def, 'pbtxt/', filename2, as_text=False)
      break
    except:
      print('\nplease, verify that destination link is correct !')

  print('CONVERSION TO BINARY DONE')

def pb2pbtxt(): 

  while 1:
    filename = raw_input('\nenter your complete .pb file link\n  >>  ')
    try:
      with gfile.FastGFile(filename,'rb') as f:
        graph_def = tf.GraphDef()
        print('\nreading the pb file')
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')
        print('\nreading file DONE !')
        break
    except : 
      print('\nplease, verify that the .pb link is correct !')

  while 1:
    filename2 = raw_input('\n\nenter the .pbtxt destination file link\n  >>  ')
    try:
      print('\nwriting the text file\n')
      tf.train.write_graph(graph_def, 'pbtxt/', filename2, as_text=True)
      break
    except:
      print('please, verify that destination link is correct !')

  print('CONVERSION TO TXT DONE')


while 1:
  a = raw_input('\nchoose the conversion :\n~~~~~~~~~~~~~~~~~~~~~\n\n  1:  pbtxt2pb\n  2:  pb2pbtxt\n\nYour choice ? ')
  if a == str(1):
    pbtxt2pb()
    print('\nBye.\n\n\n')
    break
  if a == str(2):
    pb2pbtxt()
    print('\nBye.\n\n\n')
    break
  else:
    print('wrong choice. please enter 1 or 2 !')
    pass
