#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
		create_sentences.py - Version 2.0
    Authors: Sylvain Zwolinski <sylvain-zwolinski@orange.fr>
    modified by Vincent FOUCAULT, for multi AIML files and some ups    

"""
import roslib; roslib.load_manifest('qbo_ai')
import rospy
import os
import xml.sax
import xml.sax.handler

from xml.sax.handler import ContentHandler
from xml.sax.xmlreader import Locator

path = roslib.packages.get_pkg_dir("qbo_ai")
#aimlFiles = '/home/neo/catkin_ws/src/qbo_ai/ai_fr/F.aiml'
aimlRep = '/home/neo/catkin_ws/src/qbo_ai/ai_fr/'
PAMA_AI_sentences = '/home/neo/Documents/PAMA/AI_Sentences'

class CreateSentences( xml.sax.ContentHandler ):
    
    def __init__(self):
        rospy.init_node('create_sentence')
        self.CurrentData = ""
        self.pattern = ""
        w=open(PAMA_AI_sentences, 'a')
        w.close()
        
    
    # Call when an element starts
    def startElement(self, tag, attributes):
        self.CurrentData = tag
                    
                     
    # Call when an elements ends
    def endElement(self, tag):
        if self.CurrentData == "pattern":
            w=open(PAMA_AI_sentences, 'a')
            self.pattern = self.pattern.lower()
            self.pattern = self.pattern.encode('utf-8')
            self.pattern = self.pattern.replace('*','++++++++++++').replace(' d '," d' ").replace(' l '," l' ").replace(' j '," j' ").replace(' c '," c' ").replace(' t '," t' ").replace(' qu '," qu' ")
            self.pattern = self.pattern.replace("l ","l' ")
            w.writelines(str(self.pattern+'\n'))
            print "pattern:", self.pattern
            w.close()
            
        self.CurrentData = ""

    # Call when a character is read
    def characters(self, content):
        if self.CurrentData == "pattern":
            self.pattern = content
            

    def main(self):
      # create an XMLReader
      parser = xml.sax.make_parser()
      # turn off namepsaces
      parser.setFeature(xml.sax.handler.feature_namespaces, 0)
      # override the default ContextHandler
      Handler = CreateSentences()
      parser.setContentHandler( Handler )
    
      list_dir = []
      list_dir = os.listdir(aimlRep)
      count = 0
      for file in list_dir:
          fichier = aimlRep+file
          try :
            parser.parse(fichier)
          except :
            print "erreurs dans le fichier "+file
            pass
if __name__ == '__main__':
   
    a = CreateSentences().main()

    
