ROS INDIGO
==========

some links need changes !!!

***********************************************
* all needed parts for qbo on ros hydro 12.04 *
* Work of Atom, with some corrections, *
***********************************************

sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu precise main" > /etc/apt/sources.list.d/ros-latest.list'

wget https://raw.githubusercontent.com/ros/r ... er/ros.key -O - | sudo apt-key add -

sudo apt-get update

sudo apt-get install ros-hydro-desktop-full

sudo apt-get install gstreamer0.10-pocketsphinx

sudo rosdep init

rosdep update

echo "source /opt/ros/hydro/setup.bash" >> ~/.bashrc

source ~/.bashrc

sudo apt-get install python-rosinstall

sudo chown -R <your login on ros>:users /opt/ros/hydro

***********************************************
* copy STACKS folder on ros
***********************************************

sudo apt-get build-dep pulseaudio

sudo apt-get install pulseaudio libpulse-dev

sudo apt-get install ros-hydro-camera-umd

sudo apt-get install ros-hydro-image-pipeline

chmod 777 /opt/ros/hydro/stacks/qbo_face_vision/qbo_face_recognition/faces/new_faces

chmod 777 /opt/ros/hydro/stacks/qbo_face_vision/qbo_face_recognition/faces/faces_db

sudo ln -s /opt/ros/hydro/stacks/qbo_launchers/qbo_start_service /etc/init.d/

sudo update-rc.d qbo_start_service defaults 99

sudo mv /opt/ros/hydro/stacks/qbo_mjpeg_server/Dependencies/CvBridge.h /opt/ros/hydro/include/cv_bridge

sudo apt-get install python-cherrypy3

sudo apt-get install python-xmmsclient

sudo apt-get install python-poster

sudo apt-get install xmms2

sudo apt-get install openssl

chmod 777 /opt/ros/hydro/stacks/qbo_object_recognition/objects/objects_db

chmod 777 /opt/ros/hydro/stacks/qbo_object_recognition/objects/new_objects

sudo apt-get install julius

sudo apt-get install libjulius-dev

sudo apt-get install libasound2-dev


sudo apt-get install festival

sudo cp /etc/festival.scm /etc/festival.scm.bak

sed "/aplay/c\(Parameter.set\ \'Audio_Command\ \"paplay\ \$FILE\"\)" /etc/festival.scm.bak > /etc/festival.scm

rm /etc/festival.scm.bak

sudo add-apt-repository ppa:fkrull/deadsnakes

sudo apt-get update

sudo apt-get install python2.6 python2.6-dev

sudo rmmod uvcvideo

sudo modprobe uvcvideo quirks=128

sudo gedit /etc/modprobe.d/uvcvideo.conf
then add this line "options uvcvideo quirks=128"

sudo cp -R /opt/ros/hydro/share/OpenCV /usr/share/opencv

sudo apt-get remove modemmanager

sudo usermod -a -G dialout <you user name>

chmod -R 777 /opt/ros/hydro/stacks/qbo_webi/src/xmms2/songs/

chmod -R 777 /opt/ros/hydro/stacks/qbo_webi/src/recorder/videos/

chmod 666 /opt/ros/hydro/stacks/qbo_linphone/config/linphonerc.in

export PYTHONPATH=/opt/ros/hydro/stacks/qbo_webi/src/teleoperation/sip2rtmp/p2p-sip:$PYTHONPATH



***************************
* building ! *
***************************

do rosmake on cereal, and arduqbo
do a catkin_make


*****************************
* And for XTION new model : *
*****************************

sudo apt-get install ros-hydro-openni-camera

sudo apt-get install ros-hydro-openni-launch

sudo chmod 666 /etc/openni/GlobalDefaults.ini

sudo gedit /etc/openni/GlobalDefaults.ini
remove the ";" so it should be this : UsbInterface=2
