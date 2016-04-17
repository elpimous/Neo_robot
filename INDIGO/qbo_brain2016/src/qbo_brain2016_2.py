#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
*************************************************************************
    qbo_brain2016

                         Vincent FOUCAULT       January 2016
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
from geometry_msgs.msg import Pose, Twist
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
        # Publisher to manually control the robot (e.g. to stop it)
        self.cmd_vel_pub = rospy.Publisher('cmd_vel', Twist, queue_size=1)
        
        # How long in seconds should the robot pause at each location?
        self.rest_time = rospy.get_param("~rest_time", 1)

        # Goal state return values
        self.goal_states = ['PENDING', 'ACTIVE', 'PREEMPTED', 
                       'SUCCEEDED', 'ABORTED', 'REJECTED',
                       'PREEMPTING', 'RECALLING', 'RECALLED',
                       'LOST']


        # sam fenetres, sam ch, vers entrée, face cuisine, face tv, face canapé, coté canapé
        self.waypoints = [
		[(5.196, -1.543, 0.000),(0.000, 0.000, -0.505, 0.863)],
		[(6.088, -0.356, 0.000),(0.000, 0.000, 0.238, 0.971)],
		[(2.568, 1.554, 0.000),(0.000, 0.000, 0.914, 0.405)],
		[(2.710, 2.746, 0.000),(0.000, 0.000, 0.607, 0.795)],
		[(3.120, -0.892, 0.000),(0.000, 0.000, -0.815, 0.580)],
		[(2.806, -0.877, 0.000),(0.000, 0.000, 0.514, 0.858)],
		[(2.145, 0.405, 0.000),(0.000, 0.000, 0.086, 0.996)]
			 ] # 7 waypoints
        self.docking = [[(1.205, -0.133, 0.000),(0.000, 0.000, -0.778, 0.628)]] # Dock location

        self.stopPatrol =False # for loop exciting

        # Subscribe to the move_base action server
        self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)


    def RecoveryRotation(self):
        # improving actual_pose
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

	self.goal_pose = MoveBaseGoal()    
	self.goal_pose.target_pose.header.frame_id = 'map'    
        self.goal_pose.target_pose.pose.position.x = self.targetPose[0][0]    
        self.goal_pose.target_pose.pose.position.y = self.targetPose[0][1]    
        self.goal_pose.target_pose.pose.position.z = self.targetPose[0][2]    
        self.goal_pose.target_pose.pose.orientation.x = self.targetPose[1][0]    
	self.goal_pose.target_pose.pose.orientation.y = self.targetPose[1][1]    
	self.goal_pose.target_pose.pose.orientation.z = self.targetPose[1][2]    
	self.goal_pose.target_pose.pose.orientation.w = self.targetPose[1][3]


    def DockWaypoint(self):
        # returning to dock waypoint
        while 1:
            self.targetPose = self.docking[0]
            self.Waypoints()
            self.move_base.send_goal(self.goal_pose)
            state = self.move_base.get_state()
            if state == GoalStatus.SUCCEEDED:
                rospy.loginfo("arrivé au dock waypoint !")
                break

            finished_within_time = self.move_base.wait_for_result(rospy.Duration(120))

            if not finished_within_time:
                self.move_base.cancel_goal()
                rospy.loginfo("Temps limite dépassé !")
            else :
                state = self.move_base.get_state()
                rospy.loginfo("j'ai un retour : "+str(self.goal_states[state]))

            if state != GoalStatus.SUCCEEDED:
                n = random.randint(0,6)
                rospy.loginfo("Je suis bloqué. Je passe au waypoint : "+str(n))
                self.targetPose = self.waypoints[n]
                self.Waypoints()
                self.move_base.send_goal(self.goal_pose)
            continue


    def execute(self, userdata):

        rospy.loginfo("En attente du serveur move_base...")

        # Wait 60 seconds for the action server to become available
        self.move_base.wait_for_server(rospy.Duration(20)) # 60
        
        rospy.loginfo("Robot connecté au serveur move_base.")
        rospy.loginfo("Début du test d'autonomie...")
        
        # Begin the main loop and run through a sequence of locations
        i = 0

        while not self.stopPatrol:

            # Start the robot toward the next location
            for i in range(0,len(self.waypoints)):

                self.targetPose = self.waypoints[i]

                self.Waypoints()

            	# Let the user know where the robot is going next
            	rospy.loginfo("*** En direction de l'emplacement " + str(i) + " ***")
                self.move_base.send_goal(self.goal_pose)

                # Allow 3 minutes to get there
                finished_within_time = self.move_base.wait_for_result(rospy.Duration(120)) # 180
            
                # Check for success or failure
                if not finished_within_time:
                    self.move_base.cancel_goal()
                    rospy.loginfo("Temps limite dépassé !")
                else:
                    state = self.move_base.get_state()

                i += 1

            # si la batterie nécessite une charge, 
            self.stopPatrol = True # exciting loop


        # RETURN TO DOCK WAYPOINT, before execute rth process
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
