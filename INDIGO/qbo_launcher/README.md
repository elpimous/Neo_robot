Qbo_launcher
============

A package for Qbo start services.

Automatic start and launch some packages (see launch file)

in a terminal, type :
ln -s /home/neo/catkin_ws/src/qbo_launcher/qbo_start_service /etc/init.d/
update-rc.d qbo_start_service defaults 99

Be sure to authorize the file (sudo chmod +x)
