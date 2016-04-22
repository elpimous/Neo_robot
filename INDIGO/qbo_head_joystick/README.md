Qbo_head_joystick
==========
v 1.0

#########################################################################################
#
#  You want to execute an order , like pushing a button...
#
#  move "slowly" qbo_head in some directions:
#
#	head to ground = down
#	head to sky = up
#	head right = right
#	head left = left
#
#########################################################################################
#
#  The node publish action string to the topic :
#	/head_joy
#
#########################################################################################
#
#  Vincent FOUCAULT, elpimous12@orange.fr             Avril 2016
#
#########################################################################################

to test, 2 nodes :

one with spoken directions, needs my qbo_talk (funny !)
rosrun qbo_head_joystick qbo_head_joy_with_spoken_direction.py

one with strict necessary parts, and the publish process
rosrun qbo_head_joystick qbo_head_joy.py
