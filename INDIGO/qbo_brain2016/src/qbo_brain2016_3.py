#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
*************************************************************************
    qbo_brain2016

                         Vincent FOUCAULT       March 2016
*************************************************************************
'''

import os, sys
import rospy, subprocess
import smach
import smach_ros
import actionlib
from actionlib_msgs.msg import *
from time import sleep
import random
from random import sample, choice
from geometry_msgs.msg import Pose, PoseWithCovarianceStamped, Point, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from std_msgs.msg import String
from qbo_talk.srv import Text2Speach


def run_process(command = ""):
    if command != "":
        return subprocess.Popen(command.split())
    else:
        return -1


class Leaving_Dock(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["succeded"])

    def execute(self, userdata):
        print "hello"
        os.system("rosrun qbo_navigation LeavingDock.py") # execute leavingDock, and pause everything while not finished.
        sleep(1)
        return 'succeded'



class Navigating(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["succeded"])
        # Publisher to manually control the robot
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        # Subscribe to the move_base action server
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
        # How long in seconds should the robot pause at each location?
        self.rest_time = rospy.get_param("~rest_time", 10)

        # Goal state return values
        self.goal_states = ['PENDING', 'ACTIVE', 'PREEMPTED', 
                       'SUCCEEDED', 'ABORTED', 'REJECTED',
                       'PREEMPTING', 'RECALLING', 'RECALLED',
                       'LOST']


        # sam fenetres, sam ch, vers entrée, face cuisine, face tv, face canapé, coté canapé
        self.waypoints = dict()
        self.waypoints['Salon canapé côté'] = Pose(Point(2.145, 0.405, 0.000), Quaternion(0.000, 0.000, 0.086, 0.996))
        self.waypoints['Salle_a_manger'] = Pose(Point(2.806, -0.877, 0.000), Quaternion(0.000, 0.000, 0.514, 0.858))
        self.docking = dict()
        self.docking['Salon canapé côté'] = Pose(Point(1.205, -0.133, 0.000), Quaternion(0.000, 0.000, -0.778, 0.628))
        self.stopPatrol =False # for loop exciting
        self.stopPatrol2 =False # for 2nd loop exciting

    # nettoyage de carte, par une rotation dans les 2 sens
    def RecoveryRotation(self):
    	speed_command=Twist()
	speed_command.linear.x=0.0
	speed_command.angular.z=0.5
        t = 0
        for t in range (0, 400000):
	    self.cmd_vel_pub.publish(speed_command)
            t+=1
	speed_command.angular.z=-0.5
        t = 0
        for t in range (0, 600000):
	    self.cmd_vel_pub.publish(speed_command)
            t+=1


    def Waypoints(self):

        self.RecoveryRotation() 

        self.n_waypoints = len(self.waypoints) # nombre de waypoints
        self.n = random.randint(0,(self.n_waypoints-1)) # selectionne un waypoint de façon aléatoire
        self.sequence = sample(self.waypoints, self.n_waypoints)# affiche les entêtes des waypoints
        self.location = self.sequence[self.n]
	self.goal_pose = MoveBaseGoal()    
	self.goal_pose.target_pose.header.frame_id = 'map'    
        self.goal_pose.target_pose.pose = self.waypoints[self.location]



    #  cette fonction demande au robot, de se placer à un endroit spécifique, en vue de démarrer
    #  le programme RTH
    # Si l'endroit ne peux pas être atteint, il se dirige vers un des autres waypoints.
    # une fois arrivé, il retente de se diriger vers son objectif principal, etc...

    def DockWaypoint(self):
        while not self.stopPatrol2:
            # returning to dock waypoint
            print "En direction du dock waypoint"
            dock = sample(self.docking, 1)
            self.location = dock[0]
            self.targetPose = self.docking[self.location]
	    self.goal_pose = MoveBaseGoal()    
            self.goal_pose.target_pose.header.frame_id = 'map'    
            self.goal_pose.target_pose.pose = self.targetPose
            self.move_base.send_goal(self.goal_pose)
            # Allow 1 min. to arrive at waypoint !
            self.result_within_time = self.move_base.wait_for_result(rospy.Duration(60))

            # If not succeeded in time, abort !
            if not self.result_within_time:
                rospy.loginfo("Echec > ABORT")
                self.move_base.cancel_goal()
            else :
                self.state = self.move_base.get_state()
                if self.state == GoalStatus.SUCCEEDED:
                    rospy.loginfo("dockwaypoint atteint, je quitte la boucle")
                    self.stopPatrol2 = True
                if self.state == GoalStatus.ABORTED:
                    rospy.loginfo("echec, je dois passer à un autre waypoint")
                    self.Waypoints()
                    rospy.loginfo("   En direction de l'emplacement >>> " + str(self.location))
                    self.move_base.send_goal(self.goal_pose)

        rospy.loginfo("Je suis enfin sorti de la boucle !!!!!")

    def execute(self, userdata):

        rospy.loginfo("En attente du serveur move_base...")

        # Wait 60 seconds for the action server to become available
        self.move_base.wait_for_server(rospy.Duration(60)) # 60
        rospy.loginfo("Robot connecté au serveur move_base.")
        rospy.loginfo("Début du test d'autonomie...")
        # Begin the main loop and run through a sequence of locations
        i = 0
        while not self.stopPatrol:

            print " en patrouille..."
            # Start the robot toward the next location
            for i in range(0,2): # prendre en compte 10 arrêts sur waypoints

                self.Waypoints()

            	# Let the user know where the robot is going next
            	rospy.loginfo("   En direction de l'emplacement >>> " + str(self.location))
                self.move_base.send_goal(self.goal_pose)

                # Allow 3 minutes to get there
                result_within_time = self.move_base.wait_for_result(rospy.Duration(120)) # 180
                while 1:
                  # Check for success or failure
                  if not result_within_time:
                      self.move_base.cancel_goal()
                      rospy.loginfo("Temps limite dépassé !")
                  else:
                      rospy.loginfo("move_base a envoyé un résultat !")
                      break
                i += 1

            # si la batterie nécessite une charge, 
            self.stopPatrol = True # exciting loop


        # RETURN TO DOCK WAYPOINT, before execute rth process
        print "je lance le déplacement vers le dock waypoint"
        self.DockWaypoint()

        rospy.loginfo("Arrêt du robot...")
        self.move_base.cancel_goal()
        rospy.sleep(3)
        self.cmd_vel_pub.publish(Twist())
        rospy.sleep(1)

        return 'succeded'



class Return_To_Dock(smach.State):

    def __init__(self):
        smach.State.__init__(self, outcomes=["exit"])

    def execute(self, userdata):
        os.system("roslaunch qbo_return_home return_home.launch") # return on dock, and pause everything while not finished.
        sleep(1)
        return 'exit'

def main():
    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['exit'])
    with sm:
        smach.StateMachine.add('LEAVING_DOCK', Leaving_Dock(), transitions={'succeded':'NAVIGATING'})
        smach.StateMachine.add('NAVIGATING', Navigating(), transitions={'succeded':'RTH'})
        smach.StateMachine.add('RTH', Return_To_Dock())
    sis= smach_ros.IntrospectionServer('server_name',sm,'/Brain2016')
    sis.start()

    # Execute SMACH plan
    rospy.loginfo("BRAIN launched")
    outcome = sm.execute()
    rospy.loginfo('BRAIN Finished')
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    try:
        rospy.init_node("qbo_Brain2016")
        main()
    except rospy.ROSInterruptException:
        rospy.loginfo("BRAIN node terminated.")
