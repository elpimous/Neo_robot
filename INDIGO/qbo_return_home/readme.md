Dependencies :

sudo apt-get install ros-indigo-ar-track-alvar
sudo apt-get install ros-indigo-ar-track-alvar-msgs


Howto :

Robot will find dock station with QR tags

Each tag will guide robot in room until contact with station



_____________________________________________________________________

                      Create 2 QR TAGS :

  rosrun ar_track_alvar createMarker -s 15 0  (dock tag location. Size : 15 cm, ID : 0)

_____________________________________________________________________
