ROS INDIGO
==========

some links need changes !!!

***********************************************
* all needed parts for qbo on ros indigo      *
* Work of Atom, with some corrections, *
***********************************************

install ros indigo (for me, Mint17 ! different link for ubuntu14):
 sudo sh -c '. /etc/lsb-release && echo "deb http://mirror.umd.edu/packages.ros.org/ros/ubuntu trusty main" > /etc/apt/sources.list.d/ros-latest.list' 

wget https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -O - | sudo apt-key add - 
sudo apt-get update 
sudo apt-get install ros-indigo-desktop-full

***********************************************
sudo rosdep init

rosdep update

echo "source /opt/ros/indigo/setup.bash" >> ~/.bashrc
source ~/.bashrc

sudo apt-get install python-rosinstall

sudo chown -R <your login on ros>:users /opt/ros/indigo

***********************************************
* copy STACKS folder on ros
***********************************************

sudo apt-get build-dep pulseaudio

sudo apt-get install pulseaudio libpulse-dev

sudo apt-get install ros-indigo-camera-umd

sudo apt-get install ros-indigo-image-pipeline


**** Be sure to authorize the file "qbo_start_service"(sudo chmod +x) ****
ln -s /home/neo/catkin_ws/src/qbo_launcher/qbo_start_service /etc/init.d/

sudo update-rc.d qbo_start_service defaults 99

sudo apt-get install python-cherrypy3

sudo apt-get install python-xmmsclient

sudo apt-get install python-poster

sudo apt-get install xmms2

sudo apt-get install openssl

sudo add-apt-repository ppa:fkrull/deadsnakes

sudo apt-get update

sudo apt-get install python2.7 python2.7-dev

sudo rmmod uvcvideo

sudo modprobe uvcvideo quirks=128

sudo gedit /etc/modprobe.d/uvcvideo.conf
then add this line "options uvcvideo quirks=128"

sudo cp -R /opt/ros/indigo/share/OpenCV /usr/share/opencv

sudo apt-get remove modemmanager

sudo usermod -a -G dialout <you user name>

***************************
* building ! *
***************************

do rosmake on cereal, and arduqbo
do a catkin_make


*****************************
* And for XTION new model : *
*****************************

sudo apt-get install ros-indigo-openni-camera

sudo apt-get install ros-indigo-openni-launch

sudo chmod 666 /etc/openni/GlobalDefaults.ini

sudo gedit /etc/openni/GlobalDefaults.ini
remove the ";" so it should be this : UsbInterface=2


**************************************************************************************
ERRORS CORRECTION :

*** remove bluetooth micro errors :
"bt_audio_service_open: connect() failed: Connection refused"

--> sudo apt-get purge bluez-alsa


*** 




