ROS INDIGO
==========
https://github.com/HumaRobotics/ros-indigo-qbo-packages
MANON WORK. THANKS MANON

    Install Ubuntu 14.04 (I made a bootable USB stick using http://unetbootin.sourceforge.net/ Don't forget to enable booting from USB in the boot options (for me, F2 when starting, enable USB, then F10 and boot from card reader))
    Install ROS Indigo (http://wiki.ros.org/indigo/Installation/Ubuntu)
    Install a few dependencies sudo apt-get install libpam-systemd libsystemd-daemon0 libsystemd-login0 libudev1 systemd-services udev ros-indigo-uvc-camera ros-indigo-camera-calibration-parsers ros-indigo-image-view
    add your user in dialout and video groups to be able to use USB and video ports. (My user name is qbobot, adapt to your setup) sudo usermod -a -G dialout qbobot sudo usermod -a -G video qbobot (to list the groups you are in : cat /etc/group | grep qbobot )
    Create a catkin workspace (http://wiki.ros.org/catkin/Tutorials/create_a_workspace). I called the workspace ros instead of catkin_ws, but this has no importance. In the src folder, there is a CMakeLists.txt link. Save it somewhere else, then remove src folder.
    In your catkin workspace, clone this directory in a folder named src: git clone git@github.com:HumaRobotics/ros-indigo-qbo-packages.git src Inside the src folder, put back the CMakeLists.txt you saved before.
    compile: catkin_make
    run (don't forget to do a 'source ./devel/setup.bash' in your catkin_workspace in each new terminal). Terminal 1 : roscore Terminal 2 : roslaunch qbo_arduqbo qbo_arduqbo_default.launch You can now look at published topics and move the motors and light up the mouth and nose

