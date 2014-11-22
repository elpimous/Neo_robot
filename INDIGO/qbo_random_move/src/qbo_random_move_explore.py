#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
import random

#min and max values for moves
minLinear = 0.1
maxLinear = 0.15
minAngular = -0.02
maxAngular = 0.0


def random_move():
#initialize node
    rospy.init_node('qbo_random_move_explore')
#create publisher to /cmd_vel (move base of qbo_arduqbo)
    pub = rospy.Publisher("/cmd_vel", Twist, queue_size=1)
#chose random linear and angular values
    random_linear = random.uniform(minLinear, maxLinear)
    random_angular = random.uniform(minAngular, maxAngular)
    #rospy.loginfo("Randomly moving at [%f , %f]", random_linear, random_angular)

#in an infinite loop
    while not rospy.is_shutdown():
      #change direction with probability 1 out of 10
      if random.randint(0,10) == 0:
        random_linear = random.uniform(minLinear, maxLinear)
        random_angular = random.uniform(minAngular, maxAngular)        
        #rospy.loginfo("Randomly moving at [%f , %f]", random_linear, random_angular)

      #publish Twist message to move the base
      message = Twist()
      message.linear.x=random_linear
      message.linear.y=0
      message.linear.z=0
      message.angular.x=0
      message.angular.y=0
      message.angular.z=random_angular
      pub.publish(message)

      #wait 1/10 sec, I think it's better for sensors/commands reactivity
      rospy.sleep(0.1)
#end of infinite loop


#Main instuctions
if __name__ == '__main__':
   try:
      random_move() 
   except rospy.ROSInterruptException:
      print "interrupted  !"
