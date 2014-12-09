QBO_RANDOM_MOVE_AVOIDING_OBSTACLES
==================================

THANKS FOR MANON HELP (startup package and Ros priority process !)

_____________________________________________________________________________________________________

                      roslaunch qbo_random_move neo_move_avoiding_obstacles.launch
_____________________________________________________________________________________________________
Rev1.

A move node, using both frontal SRF10, FLOOR-SENSOR, IMU, TWIST.

Package not perfect, but does the job !!!

TODO : use imu in realtime !
  when imu angle is too high, Qbo falls backward. Imu
  reaction appears after at least 1 to 2 seconds !!! 
  NOT GOOD
_______________________________________________________________
Rev2.

Imu problem solved, floor sensor too.

  Now, qbo reacts immediately regarding to risks.

Better avoiding obstacles, smooth Twist corrections.

TODO : blocked wheel recognition function
_______________________________________________________________
