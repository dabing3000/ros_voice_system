#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
 Copyright: 2016-2018 ROS小课堂 www.corvin.cn
 Author: corvin
 Description:将ASR和NLU的识别反馈结果保存到当前用户的Documents目录下的
   asr_result.txt和nlu_result.txt两个文件中.
 History:
     20180917: initial this file.
"""

import os
import rospy
import getpass
from std_msgs.msg import String

def get_user_name():
    '''return the login name of the user'''
    return getpass.getuser()


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)
        rospy.loginfo("Create ros voice system log folder path:%s", path)


def asr_callback(msg):
    filename='/home/'+ get_user_name() + '/.ros_voice_system/asr_result.txt'
    rospy.loginfo("Get asr response: %s", msg.data)
    with open(filename, 'w') as file_obj:
        file_obj.write("This is "+msg.data)


def nlu_callback(msg):
    filename='/home/'+ get_user_name() + '/.ros_voice_system/nlu_result.txt'
    rospy.loginfo("Get nlu response: %s", msg.data)
    with open(filename, 'w') as file_obj:
        file_obj.write("This is " + msg.data)


def initial():
    log_path = '/home/' + get_user_name() + '/.ros_voice_system'
    rospy.init_node("save_response_node", anonymous=True)
    mkdir(log_path)
    rospy.Subscriber("/voice_system/nlu_topic", String, asr_callback)
    rospy.Subscriber("/voice_system/tts_topic", String, nlu_callback)
    rospy.loginfo("Now ready to save response...")
    rospy.spin()

if __name__ == '__main__':
  initial()

