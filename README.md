# ros_voice_system
1.此项目整合当前中文语音环境下的所有免费系统在ROS下实现，这样大家就可以在ROS下用到免费的中文语境的语音系统了，包括语音唤醒，语音识别，语义理解，语音合成, 整合科大讯飞的语音识别、语音合成，百度语音的语音识别、语音合成，图灵机器人的语义理解等模块。（原始代码来源于ROS小课堂，部分节点作了修改）
2.建议单独建立工作空间，不要放在已有的catkin_ws中，放在home/<username>下比较好。
3.中文语音模型文件比较大，Github下载很慢，请去百度云下载，链接：https://pan.baidu.com/s/11Qk56GDHT9Al0pLRDajtnA 提取码：ot2k 下载完成后，拷贝到/ros_voice_system/src/pocketsphinx_zh/model下。
4.考虑到用户系统中可能已经安装了pocketsphinx，将此项目下的pochetsphinx包更名为pochetsphinx_zh。
5.当下载完成后，首次只需要执行工作目录下的setup_config.sh脚本即可自动安装缺少软件, 然后编译整个代码，自动配置环境变量，最后大家只需要运行voice_bringup下的launch文件即可, 直接运行roslaunch voice_bringup voice_bringup.launch 程序就可以正常运行了。一定要确认安装过程都顺利完成，不能有红色报错。如果有，请再次尝试，直到没有红色报错。
6.建议大家更换自己的帐号，这样语音的调用API次数会更多点。需要更换的包括讯飞语音的账号和对应的libmsc.so文件、图灵机器人的tuling_key、百度语音的相关账号和密码等。更换的位置一般在launch文件中。图灵机器人使用自己的账号还可以对特定问题给出特定回答，比如：你叫什么名字？我叫××机器人。
7.默认的唤醒词是“木星”，建议更换自己的唤醒词。中文唤醒词的设计方法，请参考https://blog.51cto.com/feature09/2300352，其中的“三、运行自定义的中文语言模型内容”里面的1~3。

更新日志：
2020.3.8 完成代码整理，上传Github。

