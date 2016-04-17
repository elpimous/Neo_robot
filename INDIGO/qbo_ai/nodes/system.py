#!/usr/bin/env python
# coding: utf-8

""" Plugin_system.py - Version 2.0 2016-01-01

    Created for Jarvis Project
    Authors: Sylvain Zwolinski <sylvain-zwolinski@orange.fr>
    
"""

import rospy

from diagnostic_msgs.msg import *
from qbo_system_info.srv import AskInfo
from qbo_arduqbo.srv import Test

class Plug_System():

    def __init__(self):
      
      rospy.Subscriber("/diagnostics_agg", DiagnosticArray, self.diagnostics_agg_cb)
      #rospy.init_node('plugin_system')
      
      self.listSystem = {'levelBat':'0', 'statBat':'', 'infoBat':'', 'autonBat':'', 'internet':'no','ipeth':'0', 'ipwlan':'0', 'camera1':'no', 'camera2':'no', 'xtion':'no', 'clavier':'no', 'souris':'no', 'Qboard3':'no', 'Qboard1':'no', 'Qboard2':'no'}
      
      #Batterie
      self.levelBat = 0
      self.statBat = ""
      self.infoBat = ""
      self.autonBat = "" 
        
      #Capteur Floor
      self.distFloor = 0
      self.paramFloorMin = 0
      self.paramFloorMax = 0
      self.infoFloor = ""
        
      #Capteurs SRF10 Front Right
      self.distSrf10FR = 0
      self.paramSrf10FR = 0
      self.infoSrf10FR = ""
        
      #Capteurs SRF10 Front Left
      self.distSrf10FL = 0
      self.paramSrf10FL = 0
      self.infoSrf10FL = ""
        
      #Capteurs SRF10 Back Right
      self.distSrf10BR = 0
      self.paramSrf10BR = 0
      self.infoSrf10BR = ""
        
      #Capteurs SRF10 Back Left
      self.distSrf10BL = 0
      self.paramSrf10BL = 0
      self.infoSrf10BL = ""
      
      #Adresse IP
      self.internet = 'no' 
      self.ipeth = 0
      self.ipwlan = 0
      
      #USB 
      self.camera1 = 'no'
      self.camera2 = 'no'
      self.xtion = 'no'
      self.clavier = 'no'
      self.souris = 'no'
       
    def aiml_system(self):
        return self.listSystem
    
    def netconf(self):
        rospy.wait_for_service("/pluginsystem");
        service_pluginsystem = rospy.ServiceProxy('/pluginsystem', AskInfo)
        info = service_pluginsystem("netconf")
        ip = str(info.info)
        ip = ip.replace("eth0","").replace("wlan0","").replace(" ","").replace(".",". ")
        lines = ip.split("\n")
        try:
            if len(lines)>= 2 :
              if lines[0] :
                self.ipeth = lines[0]
                self.listSystem['ipeth']= self.ipeth
              if lines[1] :
                self.ipwlan = lines[1]
                self.listSystem['ipwlan']= self.ipwlan
            elif len(lines) == 1 :
              if lines[0] :
                self.ipeth = lines[0]
                self.listSystem['ipeth']= self.ipeth
        except:
            print "Erreur"
            pass
            
    def web(self):
        rospy.wait_for_service("/pluginsystem");
        service_pluginsystem = rospy.ServiceProxy('/pluginsystem', AskInfo)
        info = service_pluginsystem("internet")
        net = str(info.info)
        lines = net.split("\n")
        try:
          if len(lines) <= 2 :
            self.internet = str('ok')
            self.listSystem['internet']= self.internet
        except:
            print "Erreur"
            pass
             
    def testUsb(self):
          rospy.wait_for_service("/pluginsystem");
          service_pluginsystem = rospy.ServiceProxy('/pluginsystem', AskInfo)
          info = service_pluginsystem("UsbInfo")
          listMaterielUsb = ['Keyboard','Camera','Camera','ASUS','Cypress']
          self.listSystem['clavier']='no'
          self.listSystem['camera1']='no'
          self.listSystem['camera2']='no'
          self.listSystem['xtion']='no'
          self.listSystem['souris']='no'
          info = str(info).replace("info: ","")
          info = str(info).splitlines()
          print len(info)
          print len(listMaterielUsb)
          alreadySeen = False    
          for i in range(0,len(info)):
            line = info[i].split(" ")
            #print line[6:]
            for z in range(0,len(line)):
              if z >= 6 :
                for y in range(0,len(listMaterielUsb)):
                  try:
                    if listMaterielUsb[y] == line[z]:
                      if listMaterielUsb[y] == str('Keyboard'):
                        self.listSystem['clavier']='yes'
                        break 
                      elif listMaterielUsb[y] == str('Camera') and not alreadySeen :
                        self.listSystem['camera1']='yes'
                        alreadySeen = True
                        break 
                      elif listMaterielUsb[y] == str('Camera'):
                        self.listSystem['camera2']='yes'
                        break
                      elif listMaterielUsb[y] == str('ASUS'):
                        self.listSystem['xtion']='yes'
                        break
                      elif listMaterielUsb[y] == str('Cypress'):
                        self.listSystem['souris']='yes'
                        break
                  except:
                    print "Erreur"
                    pass
    
    def testArduqbo(self):
        service_test_client = rospy.ServiceProxy('/qbo_arduqbo/test_service', Test)
        #rospy.loginfo("Waiting for_service test_service...  ")
        rospy.wait_for_service("/qbo_arduqbo/test_service");
        testResponse = service_test_client()
        testDic=['Gyroscope','Accelerometer','LCD','Qboard3','Qboard1','Qboard2','rightMotor','leftMotor']
        #print str(testResponse)
        if testResponse.Gyroscope == True :
            self.listSystem['Gyroscope']= "ok"
        if testResponse.Accelerometer == True :
            self.listSystem['Accelerometer']= "ok"
        if testResponse.LCD == True :
            self.listSystem['LCD']= "ok"
        if testResponse.Qboard3 == True :
            self.listSystem['Qboard3']= "ok"     
        if testResponse.Qboard2 == True :
            self.listSystem['Qboard2']= "ok"
        if testResponse.Qboard1 == True :
            self.listSystem['Qboard1']= "ok"
        if testResponse.rightMotor == True :
            self.listSystem['rightMotor']= "ok"
        if testResponse.leftMotor == True :
            self.listSystem['leftMotor']= "ok"
                    
    def diagnostics_agg_cb(self,data):
        
        #Batterie
            #Tension batterie
        self.levelBat = data.status[1].values[0].value
        self.listSystem['levelBat']= self.levelBat
            #Etat batterie/chargeur(Binaire)
        self.statBat = data.status[1].values[1].value
        self.listSystem['statBat']= self.statBat
            #Information batterie
        self.infoBat = data.status[1].values[2].value
        self.listSystem['infoBat']= self.infoBat
            #Etat autonomie batterie
        self.autonBat = data.status[1].message
        self.listSystem['autonBat']= self.autonBat


if __name__ == '__main__':
    try:
        Plug_System()
        rospy.spin()
    except rospy.ROSInterruptException: pass   
    
