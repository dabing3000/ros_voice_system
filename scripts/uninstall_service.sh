#!/bin/bash

# Copyright: 2016-2018 ROS小课堂 www.corvin.cn
# Author: corvin
# Description: Uninstall voice_system.service.
# History:
#    20181129:initial this bash file.

pid=`ps -ef|grep voice_bringup.launch|grep -v grep|awk '{print $2}'`
if [ -n "$pid" ]
then
    /usr/sbin/voice_system_stop
fi

sudo systemctl disable voice_system.service

sudo rm /usr/sbin/voice_system_start
sudo rm /usr/sbin/voice_system_stop
sudo rm /usr/sbin/voice_system_restart

sudo rm /lib/systemd/system/voice_system.service

exit 0
