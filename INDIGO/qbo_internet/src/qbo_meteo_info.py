#!/usr/bin/env python
# coding: utf-8


# Author: Vincent FOUCAULT
# use of web meteo api, for weather informations
# end march 2016


import rospy
import requests
import urllib2
import json
from std_msgs.msg import String

class Meteo():

    def __init__(self):
        
        rospy.init_node('qbo_meteo_info')
        # The rate at which to publish the diagnostic sensor back left
        self.rate = rospy.get_param("~rate", 0.1)
        # Convert to a ROS rate
        self.d = rospy.Duration(1800, 0) # 1800  each 30 minuts

        # enter here your PERSONAL KEY
        self.myKey = "117564cb7eb2c406"
        # meteo icons name will serve in emotion statut creation
        self.happyDic = ['clear','cloudy','mostlycloudy','mostlysunny','partlycloudy','partlysunny','sunny']
        self.neutralDic = ['fog','hazy','chanceflurries','chancerain','chancesleet','chancesnow','chancetstorms']
        self.sadDic = ['sleet','rain','snow','tstorms','flurries']
        self.meteo_pub = rospy.Publisher ('/meteo_info',String, queue_size = 1)
        self.emotion_pub = rospy.Publisher ('/emotion_statut',String, queue_size = 1)
        self.emotion = ""


    def meteo(self):
        while not rospy.is_shutdown():

            # weather, this day
          try :
            self.today = urllib2.urlopen('http://api.wunderground.com/api/'+self.myKey+'/geolookup/conditions/lang:FR/q/France/Evreux.json')
            json_string = self.today.read()
            parsed_json = json.loads(json_string)
            self.temp_c = (str(parsed_json['current_observation']['temp_c'])).encode('utf8')
            self.weather = (parsed_json['current_observation']['weather']).encode('utf8')
            self.humidity = (str(parsed_json['current_observation']['relative_humidity'])).encode('utf8')
            self.wind = (str(parsed_json['current_observation']['wind_kph'])).encode('utf8')
            self.icon_statut = (parsed_json['current_observation']['icon']).encode('utf8')
            #emotion
            if str(self.icon_statut) in self.happyDic :
              self.emotion = "happy"
            elif str(self.icon_statut) in self.neutralDic :
              self.emotion = "neutral"
            elif str(self.icon_statut) in self.sadDic :
              self.emotion = "sad"
            else :
              self.emotion = "neutral"
            self.today.close()

	    # weather, tomorrow
	    self.tomorrow = urllib2.urlopen('http://api.wunderground.com/api/'+self.myKey+'/conditions/forecast/lang:FR/q/France/Evreux.json')
	    json_string2 = self.tomorrow.read()
	    parsed_json2 = json.loads(json_string2)
	    self.tomorrowWeather = (parsed_json2['forecast']['simpleforecast']['forecastday'][1]['conditions']).encode('utf8')
	    self.tomorrowTemp_c_low = (str(parsed_json2['forecast']['simpleforecast']['forecastday'][1]['low']['celsius'])).encode('utf8')
	    self.tomorrowTemp_c_high = (str(parsed_json2['forecast']['simpleforecast']['forecastday'][1]['high']['celsius'])).encode('utf8')


            #  weather_feed
            self.meteo = ("TODAY :\nWeather : "+self.weather+"\nTemp : "+self.temp_c+"\nHumidity : "+self.humidity+"\nWind : "+self.wind+"\n\nTOMORROW :"+"\nTomorrow_Weather : "+self.tomorrowWeather+"\nTomorrow_Temp_Low : "+self.tomorrowTemp_c_low+"\nTomorrow_Temp_High : "+self.tomorrowTemp_c_high)

            #  emotion_feed
            self.emotional_statut = ("My actual emotional state is :\n"+self.emotion)

	    #  publishs
            self.meteo_pub.publish(self.meteo)
            self.emotion_pub.publish(self.emotional_statut)
            print "envoyé"

          except :
            no_network = "Can't access network, next try in 30 min"
            self.meteo_pub.publish(no_network)
            self.emotion_pub.publish(no_network)

          rospy.sleep(self.d)

if __name__ == '__main__':

    try:
        meteo = Meteo()
        meteo.meteo()
        rospy.spin()
    except rospy.ROSInterruptException: pass

