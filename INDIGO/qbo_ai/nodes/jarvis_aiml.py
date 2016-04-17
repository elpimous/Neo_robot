#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Neo_aiml.py - Version 2.0 2016-01-20

    Created for Neo Project
    Authors: Sylvain Zwolinski <sylvain-zwolinski@orange.fr>
    
"""

import rospy 
import roslib; roslib.load_manifest('qbo_ai')
import aiml
import sys
import os,shutil
import time
import subprocess

from system import Plug_System
from face_recognition.msg import FaceRecognitionAction, FaceRecognitionGoal, FaceRecognitionResult
from qbo_face_msgs.msg import FacePosAndDist
from qbo_talk.srv import Text2Speach
from lib_qbo_pyarduqbo import qbo_control_client

from actionlib.msg import *
from std_msgs.msg import String

global path

path = roslib.packages.get_pkg_dir("qbo_ai")



def speak_this(text): 
  global client_speak
  print "réponse : ",str(text)
  client_speak(str(text))
  

def run_process(command = ""):

    if command != "":
        return subprocess.Popen(command.split())
    else:
        return -1
  
class Neo_Chat():
        
    def __init__(self):
        global client_speak
        global path
                    
        client_speak = rospy.ServiceProxy("/say_fr1", Text2Speach) # for french
        rospy.Subscriber("/qbo_face_tracking/face_pos_and_dist", FacePosAndDist, self.face_callback)
        rospy.Subscriber('listened', String, self.listen_callback)    
        os.system("amixer -c 1 sset Mic,0 nocap")
        run_process("rosrun qbo_system_info plugin_system.py")
        
        #Import des fonctions
        self.kernel = aiml.Kernel()
        self.system = Plug_System()
        self.controller = qbo_control_client()
        
        #Paramétres pour la Recognition
        self.startNeo = False
        self.startNeoOk = False
        self.face_stabilizer =0
        self.stabilizer_max = 10
        self.stabilizer_thr = 7
        self.distance_head_max = 1.5
        self.recognized_name = ""
        self.recog_name_certainty = 0.94
        self.launch_reco = False
        self.launch_listen = False
        self.time_of_stop = 0
        self.stop_reco = False
        wait_time = 20
        
        #Paramétre wake_up
        self.OFFSET_X = 0.15
        
        #Paramétre déplacement
        self.bot_move = False
        
        #Paramétres pour l'AIML
        self.question =''
        sessionTest = rospy.get_param("~sessionTest", True)
        self.sessionId = 'unknown'
        self.last_undetected = False
        self.diagnostics ={}
        
        
        self.ref_file = os.walk(path+'/reference_file')  
        fileBot = path+'/config/setBotPredicate.txt'
        fileBotParameter = path+'/config/setBotParameter.txt'
        
        self.fileParameterId = path+'/'+ self.sessionId +'/parameter/parameterId.txt'
        self.fileParameterAiml = path+'/'+self.sessionId+'/parameter/parameterAiml.txt'
        self.fileConversationId = path+'/'+self.sessionId+'conversation/conversationId.txt'
        
        filesession = path+'/'+str(self.sessionId)+'/sessionData.txt'
        
        #Permet de rappeller les infos du bot
        f = open(fileBot)
        for line in f.readlines():
          try:
            line = line.replace("\n","")
            parts = line.split("|")
                    
            name = parts[0]
            value = parts[1]
            self.kernel.setBotPredicate(str(name),str(value))
            print "kernel.setBotPredicate("+str(name)+", "+str(value)+")"
          except Exception:
            print 'Excepcion: '
            pass
          f.close()
        
        if os.path.isfile("/home/neo/catkin_ws/src/qbo_ai/neo_ai_fr.brn") and not sessionTest:
              self.kernel.bootstrap(brainFile = "/home/neo/catkin_ws/src/qbo_ai/neo_ai_fr.brn")
        else:
            self.kernel.bootstrap(learnFiles="/home/neo/catkin_ws/src/qbo_ai/neo_ai_fr/*.aiml")# charge tous les fichiers aiml
            self.kernel.saveBrain("/home/neo/catkin_ws/src/qbo_ai/neo_ai_fr.brn")
        
        self.system.netconf()
        self.system.web()
        self.system.testUsb()
        self.system.testArduqbo()
        
        self.diagnostics = self.system.aiml_system()
        
        cleSyst = list(self.diagnostics.keys())
        for y in range(0,len(cleSyst)):
          try:
            self.kernel.setPredicate(str(cleSyst[y]),str(self.diagnostics[cleSyst[y]]))
            print str(cleSyst[y]) +' : '+str(self.diagnostics[cleSyst[y]])
          except Exception:
            pass
        
        
        autonBat = self.kernel.getPredicate("autonBat")
        reponse = self.kernel.respond('START')
        speak_this(reponse)
        rospy.sleep(4)
        self.startNeo = True
        self.time_of_stop = rospy.Time.now()
        
        #Boucle principale de l'AIML de Neo
        while not rospy.is_shutdown() :
          
          self.set_period()
          
          time_diff = rospy.Time.now() - self.time_of_stop
          
          self.diagnostics = self.system.aiml_system()
          
          autonBat = self.kernel.getPredicate("autonBat")
          
                    
          #Boucle secondaire : conversation avec la personne reconnu         
          if self.face_stabilizer >= self.stabilizer_thr and self.recognized_name != "" and self.recognized_name != "unknown" and not self.last_undetected:
              print "j'ouvre le dossier de :"+str(self.recognized_name)    
              self.sessionId = str(self.recognized_name)
              
              self.fileParameterId = path+'/'+ self.sessionId +'/parameter/parameterId.txt'
              self.fileParameterAiml = path+'/'+self.sessionId+'/parameter/parameterAiml.txt'
              self.fileConversationId = path+'/'+self.sessionId+'/conversation/conversationId.txt'
              self.last_undetected = True
              self.open_data(self.fileParameterId)
              self.open_data(self.fileParameterAiml)
              self.set_period()
              
              client_quit = self.kernel.getPredicate("aurevoir",self.sessionId)
              client_move = self.kernel.getPredicate("move",self.sessionId)
              sessionData = self.kernel.getSessionData(self.sessionId)
              
              reponse = self.kernel.respond('CONNECT',self.sessionId)
              speak_this(reponse)
              
              self.system.testUsb()
              while not rospy.is_shutdown() and not (client_quit == str("oui") or client_move == str("1")):
                  time_diff = rospy.Time.now() - self.time_of_stop
                  client_quit = self.kernel.getPredicate("aurevoir",self.sessionId)
                  client_date = self.kernel.getPredicate("date",self.sessionId)
                  client_period = self.kernel.getPredicate("period",self.sessionId)
                  client_move = self.kernel.getPredicate("move",self.sessionId)
                  sessionData = self.kernel.getSessionData(self.sessionId)
                  
                  if self.question != '' and self.last_undetected:
                                      
                    print client_period
                    cleSyst = list(self.diagnostics.keys())
                    for y in range(0,len(cleSyst)):
                      try:
                        self.kernel.setPredicate(str(cleSyst[y]),str(self.diagnostics[cleSyst[y]]), self.sessionId)
                      except Exception:
                        pass
                  
                    reponse = self.kernel.respond(self.question, self.sessionId)
                    speak_this(reponse) 
                    self.question = ''
                                    
                  elif time_diff.to_sec()>wait_time and not self.stop_reco :
                    self.kernel.setPredicate("aurevoir","oui",self.sessionId)
              
              self.question = ''
              if client_move == str("1") :
                  self.bot_move = True
                  self.kernel.setPredicate("aurevoir","oui",self.sessionId)
              self.kernel.setPredicate("aurevoir","",self.sessionId)
              self.last_undetected = False      
              print "je sauvegarde"
              self.kernel.saveBrain("/home/Neo/catkin_ws/src/qbo_ai/Neo.brn")
              self.save_file(self.sessionId,sessionData)
              #self.save_conversation(sessionData)
              rospy.sleep(3)
              
    
          #Boucle secondaire : aprentissage d'une personne          
          elif self.face_stabilizer >= self.stabilizer_thr and self.recognized_name == "unknown" and not self.last_undetected :
              self.last_undetected = True
              reponse = self.kernel.respond('CONNECT')
              speak_this(reponse)
              
              client_quit = self.kernel.getPredicate("aurevoir")
              client_move = self.kernel.getPredicate("move")
              sessionData = self.kernel.getSessionData()
                            
              self.system.testUsb()
              while not rospy.is_shutdown() and not (client_quit == str("oui") or client_move == str("1")):
                  time_diff = rospy.Time.now() - self.time_of_stop
                  client_quit = self.kernel.getPredicate("aurevoir")
                  client_date = self.kernel.getPredicate("date")
                  client_period = self.kernel.getPredicate("period")
                  client_move = self.kernel.getPredicate("move")
                  sessionData = self.kernel.getSessionData()
                  
                  if self.question != '' and self.last_undetected:
                                      
                    print client_period
                    cleSyst = list(self.diagnostics.keys())
                    for y in range(0,len(cleSyst)):
                      try:
                        self.kernel.setPredicate(str(cleSyst[y]),str(self.diagnostics[cleSyst[y]]))
                      except Exception:
                        pass
                  
                    reponse = self.kernel.respond(self.question)
                    speak_this(reponse) 
                    self.question = ''
                                    
                  elif time_diff.to_sec()>wait_time and not self.stop_reco :
                    self.kernel.setPredicate("aurevoir","oui")
              
              self.question = ''
              if client_move == str("1") :
                  self.bot_move = True
                  self.kernel.setPredicate("aurevoir","oui")
              self.kernel.setPredicate("aurevoir","")
              self.last_undetected = False      
              print "je sauvegarde pas car je ne le connais pas"                   
          
          elif time_diff.to_sec()>wait_time and not self.stop_reco and not self.bot_move :
              run_process("rosnode kill /qbo_face_tracking")
              run_process("rosnode kill /qbo_face_following")
              self.stop_reco = True
              self.last_undetected = False
              self.wake_up()
              
          #Mise à jour des diagnostiques de ROS dans l'Aiml              
          cleSyst = list(self.diagnostics.keys())
          for y in range(0,len(cleSyst)):
              try:
                self.kernel.setPredicate(str(cleSyst[y]),str(self.diagnostics[cleSyst[y]]))
              except Exception:
                pass
    
    #Fonction d'ouverture des fichiers coresspondant à la personne
    def open_data(self,file_param):
        f = open(file_param)
        for line in f.readlines():
          try:
            line = line.replace("\n","")
            parts = line.split("|")  
            name = parts[0]
            value = parts[1]
            self.kernel.setPredicate(str(name),str(value),str(self.sessionId))
            print "kernel.setPredicate("+str(name)+", "+str(value)+", "+str(self.sessionId)+")"
          except Exception:
            print 'Excepcion: '
            pass
        f.close()                        
    
    #Fonction d'enregistrement de la conversation
    def save_conversation(self,sessionData):
        cle= list(sessionData.keys())
        f= open(self.fileConversationId, "w")
        for x in range(0,len(cle)) :
          try:
            if cle[x] == str('_outputHistory') :
              print str(cle[x]) + " : " + str(sessionData[cle[x]])
              f.writelines(str(cle[x])+":"+str(sessionData[cle[x]])+"\n")         
            elif cle[x] == str('_inputHistory') :
              print str(cle[x]) + " : " + str(sessionData[cle[x]])
              f.writelines(str(cle[x])+":"+str(sessionData[cle[x]])+"\n")
            elif cle[x] == str('_inputStack') :
              print str(cle[x]) + " : " + str(sessionData[cle[x]])
              f.writelines(str(cle[x])+":"+str(sessionData[cle[x]])+"\n")
            else :
              pass
              #print str(cle[x]) +' : '+ sessionData[cle[x]]
                        
          except Exception:
            pass
        f.close()
    
    #Fonction d'enregistrement des paramétres
    def save_file(self,sessionId,sessionData):
      global path
      id_file = os.walk(path+'/'+sessionId+'/parameter')
      lstRef = []
      lstId = []  
      for FileRef in self.ref_file:
        for x in FileRef[2]:
          if x.endswith('txt'):
            print FileRef[0]+"/"+ x
            lstRef.append(x)
            
      for FileId in id_file:
        for y in FileId[2]:
          if y.endswith('txt'):
            print FileId[0]+"/"+ y
            lstId.append(y)
  
      cle= list(sessionData.keys())
      print len(cle)
      print sessionData
      for z in range(0,len(lstRef)):
        f = open(FileRef[0]+"/"+lstRef[z])
        w = open(FileId[0]+"/"+lstId[z], "w")
        print FileRef[0]+"/"+lstRef[z]
        print FileId[0]+"/"+lstId[z]
        
        for line in f.readlines():
          try:
            line = line.replace("\n","")
            parts = line.split("|")
                
            name = parts[0]
            value = parts[1]
            #print name
            find = False
            for x in range(0,len(cle)) :
              try:
                if name ==  str(cle[x]):
                  find = True
                  #print "ok"
                  write= sessionData[cle[x]]
                  write=write.encode('utf-8')
                  w.writelines(name+"|"+write+"\n")
                  #w.writelines(name+"|"+sessionData[cle[x]]+"\n")
              except Exception:
                pass
            if not find :
              #print "J'écris sans rien"
              w.writelines(name+"|"+"\n")   
          except Exception:
            print "Aie"
            pass  
                
        f.close()
        w.close() 
                                    
    #Fonction d'écoute (Listen)  
    def listen_callback(self,msg):
        print "question = ",msg.data
        self.question = msg.data

    #Ensemble de fonction pour la recognition (Following/Tracking/Recogition)
    def face_callback(self,data):
        if self.startNeo and not self.startNeoOk :
            rospy.set_param("/qbo_face_following/move_head", True)
            self.startNeoOk = True
               
        if data.face_detected==True and self.face_stabilizer<self.stabilizer_max and data.distance_to_head<self.distance_head_max : 
          self.face_stabilizer+=0.2
          
        elif data.face_detected==True and data.distance_to_head<self.distance_head_max and self.bot_move :
          run_process("rosnode kill /qbo_random_move")
          self.kernel.setPredicate("move","",self.sessionId)
          self.bot_move = False
          
        elif data.face_detected==True and self.face_stabilizer >= self.stabilizer_max and not self.launch_reco :
          self.launch_reco = True
          self.launch_listen = True
          recog = self.get_name()
          os.system("amixer -c 1 sset Mic,0 cap")
        
        elif data.face_detected==True and self.face_stabilizer >= self.stabilizer_max :
          self.time_of_stop = rospy.Time.now()  
    
        elif data.face_detected==False and self.face_stabilizer>0 :
          self.face_stabilizer-=2
  
        elif self.face_stabilizer<= 0 and self.launch_listen :
          self.question = ''
          self.launch_reco = False
          
          self.launch_listen = False
          rospy.sleep(2)
          os.system("amixer -c 1 sset Mic,0 nocap")
    
    def get_name(self):
            
        reco = actionlib.SimpleActionClient("face_recognition", FaceRecognitionAction)
    
        rospy.loginfo("Connected to face recognition server")
        reco.wait_for_server(rospy.Duration(10))
    
        reco_goal = FaceRecognitionGoal()
        reco_goal.order_id = 0
        reco_goal.order_argument="none"
        reco.send_goal(reco_goal)
    
        rospy.loginfo("Waiting the result to face recognition server")
        finished_within_time = reco.wait_for_result(rospy.Duration(2))
    
        if not finished_within_time:
            self.recognized_name = "unknown"
            reco.cancel_goal()
            #self.kernel.setPredicate('name',str(self.recognized_name))
            #self.kernel.setPredicate('confidence','00')
            return "unknown"
        
        else:
          state = reco.get_state()        
          result = reco.get_result()
          name = result.names
          confidence = "%.2f" %result.confidence
          confidence = float(confidence)*100
          confidence = int(confidence)
          
          name = str(name).replace("[","").replace("]","").replace("'","").capitalize()
      
        if confidence >= self.recog_name_certainty :
          rospy.loginfo("Il s'agit de :" + str(name))
          rospy.loginfo("Avec une reconnaissance de :" + str(confidence)+"%")
          self.kernel.setPredicate('valConfidence',str(confidence),str(name))
          self.kernel.setPredicate('name',str(name),str(name))
          self.kernel.setPredicate('confidence','ok',str(name))
          self.recognized_name = name 
          return str(name)
    
    def set_name(self):
    
        reco = actionlib.SimpleActionClient("face_recognition", FaceRecognitionAction)
        
        rospy.loginfo("Connected to face recognition server")
        reco.wait_for_server(rospy.Duration(10))
    
        reco_goal = FaceRecognitionGoal()
        reco_goal.order_id = 0
        reco_goal.order_argument="none"
        reco.send_goal(reco_goal)
        
        rospy.loginfo("Waiting the result to face recognition server")
        finished_within_time = reco.wait_for_result(rospy.Duration(4))
    
    #Fonction d'interprétation du moment de la journée
    def set_period(self):
        #print self.sessionId 
        if time.strftime("%H",time.localtime()) >= str(22):
            self.kernel.setPredicate('period',"nuit soiree",self.sessionId)
        elif time.strftime("%H",time.localtime()) >= str(20):
            self.kernel.setPredicate('period',"soiree",self.sessionId)
        elif time.strftime("%H",time.localtime()) >= str(19):
            self.kernel.setPredicate('period',"début de soiree",self.sessionId)
        elif time.strftime("%H",time.localtime()) >= str(17):
            self.kernel.setPredicate('period',"fin de journee",self.sessionId)
        elif time.strftime("%H",time.localtime()) >= str(13):
            self.kernel.setPredicate('period',"journee",self.sessionId)
        elif time.strftime("%H",time.localtime()) >= str(12):
            self.kernel.setPredicate('period',"midi",self.sessionId)
        elif time.strftime("%H",time.localtime()) >= str(8):
            self.kernel.setPredicate('period',"matinee",self.sessionId)
        elif time.strftime("%H",time.localtime()) >= str(6):
            self.kernel.setPredicate('period',"début de matinee",self.sessionId)
        else :
            self.kernel.setPredicate('period',"journee",self.sessionId)        
    
    def wake_up(self):
        get_all_distances=self.controller.getAllDistances()
        
        frontalRight = get_all_distances[0][0]
        print float(frontalRight)
        if frontalRight == 0.0 :
            frontalRight = 1.2
        else :
            frontalRight = frontalRight - self.OFFSET_X   
        
        frontalLeft = get_all_distances[1][0]
        print float(frontalLeft)
        if frontalLeft == 0.0 :
            frontalLeft = 1.2
        else :
            frontalLeft = frontalLeft - self.OFFSET_X
            
        backRight = get_all_distances[2][0]
        print float(backRight)
        if backRight == 0.0 :
            backRight = 1.2
        else :
            backRight = backRight - self.OFFSET_X
        
        backLeft = get_all_distances[3][0]
        print float(backLeft)
        if backLeft == 0.0 :
            backLeft = 1.2
        else :
            backLeft = backLeft - self.OFFSET_X
        
        while not rospy.is_shutdown() and self.stop_reco:
            get_all_distances=self.controller.getAllDistances()     
      
            if (get_all_distances[0][1] and get_all_distances[0][0]<frontalRight) or (get_all_distances[1][1] and get_all_distances[1][0]<frontalLeft) or (get_all_distances[2][1] and get_all_distances[2][0]<backRight) or (get_all_distances[2][1] and get_all_distances[2][0]<backLeft):
                self.time_of_stop = rospy.Time.now()
                self.stop_reco = False
                run_process("roslaunch qbo_ai wake_up.launch")
            rospy.sleep(1)
        print "Je suis sorti de la boucle"        
                                        	    	
if __name__ == "__main__":
    try:
        rospy.init_node('Neo_Chat', anonymous=False)
        Neo_Chat()
        rospy.spin()
    except Exception, e:
      print 'Excepcion: ', e
      exit()
