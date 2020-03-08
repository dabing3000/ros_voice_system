#!/bin/bash

# Copyright: 2016-2018 ROS小课堂 www.corvin.cn
# Author: corvin
# Description: install voice system service to /lib/systemd/system,this will
#    auto roslaunch voice system when poweron.
# History:
#    20181129: initial this bash file.

sudo cp ./voice_system_service/voice_system_start /usr/sbin/
sudo cp ./voice_system_service/voice_system_stop /usr/sbin/
sudo cp ./voice_system_service/voice_system_restart /usr/sbin/
sudo cp ./voice_system_service/voice_system.service /lib/systemd/system/

sudo systemctl enable voice_system.service

exit 0
