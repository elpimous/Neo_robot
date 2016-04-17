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

# enter here your PERSONAL KEY
myKey = "117564cb7eb2c406"

# weather, this day
f = urllib2.urlopen('http://api.wunderground.com/api/'+myKey+'/geolookup/conditions/lang:FR/q/France/Evreux.json')
json_string = f.read()
parsed_json = json.loads(json_string)
temp_c = (str(parsed_json['current_observation']['temp_c'])).encode('utf8')
weather = (parsed_json['current_observation']['weather']).encode('utf8')
humidity = (str(parsed_json['current_observation']['relative_humidity'])).encode('utf8')
wind = (str(parsed_json['current_observation']['wind_kph'])).encode('utf8')
icon_statut = (parsed_json['current_observation']['icon']).encode('utf8')


# weather, tomorrow
forecast = urllib2.urlopen('http://api.wunderground.com/api/'+myKey+'/conditions/forecast/lang:FR/q/France/Evreux.json')
json_string2 = forecast.read()
parsed_json2 = json.loads(json_string2)
tomorrowWeather = parsed_json2['forecast']['simpleforecast']['forecastday'][1]['conditions']
tomorrowTemp_c_low = parsed_json2['forecast']['simpleforecast']['forecastday'][1]['low']['celsius']
tomorrowTemp_c_high = parsed_json2['forecast']['simpleforecast']['forecastday'][1]['high']['celsius']

def meteo():

    print "Pour aujourd'hui, %s, une température de %s degrés, une humidité à %s, et un vent à %s Kilomètres par heure" % (str(weather).lower(), (temp_c), (humidity), (wind))

    # meteo icons name will serve in emotion statut creation
    happyDic = ['clear','cloudy','mostlycloudy','mostlysunny','partlycloudy','partlysunny','sunny']
    neutralDic = ['fog','hazy','chanceflurries','chancerain','chancesleet','chancesnow','chancetstorms']
    sadDic = ['sleet','rain','snow','tstorms','flurries']
    if str(icon_statut) in happyDic :
      emotion = "happy"
    elif str(icon_statut) in neutralDic :
      emotion = "neutral"
    elif str(icon_statut) in sadDic :
      emotion = "sad"
    else :
      emotion = "neutral"
    f.close()

    meteo_pub = rospy.Publisher ('/emotion',String, queue_size = 1)
    meteo_pub.publish(str("hello"))
    print "je publie"
    meteo_pub.publish(str("hello2"))
    print "je publie"

def tomorrowMeteo():
    print "Bon, demain, %s. Le thermomètre affichera %s degrés au plus bas, et montera à %s degrés" % (str(tomorrowWeather), str(tomorrowTemp_c_low), str(tomorrowTemp_c_high))
    forecast.close()


if __name__ == '__main__':

    rospy.init_node("qbo_meteo")
    try:
        meteo = meteo()
        tomorrowMeteo = tomorrowMeteo()
        rospy.spin()
    except rospy.ROSInterruptException: pass


