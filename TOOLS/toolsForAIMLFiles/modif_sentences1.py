#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

class CreateSentences():
    
    def __init__(self):
	self.PAMA_AI_sentences = '/home/neo/Documents/PAMA/AI_Sentences'
        self.PAMA_AI_without_single_word = '/home/neo/Documents/PAMA/AI_Sentences_W_SW'

    def main(self):
      open_file = open(self.PAMA_AI_sentences, "r")
      open_file2 = open(self.PAMA_AI_without_single_word, "w")
      open_file
      open_file2
      for lign in open_file:
          # remove lign with just one word
          a = len(lign.split())
          if a < 2 :
            print " removing smallest sentence"
            continue
          if "++++++++++++" in lign:
            print " removing ++++++++++++"
            continue
          if "singulier" in lign:
            print " removing word : singulier"
            continue
          lines_seen = set()
          if lign in lines_seen: # not a duplicate
            print " removing duplicate sentences"
            continue
          lines_seen.add(lign)
          open_file2.write(lign)
      open_file.close()
      open_file2.close()

      uniqlines = set(open(self.PAMA_AI_without_single_word).readlines())
      bar = open('/home/neo/Documents/PAMA/AI_Sentences_Last', 'w').writelines(set(uniqlines))
      #bar.close()

if __name__ == '__main__':
   
    a = CreateSentences().main() 
