#!/usr/bin/env python
import  rospy
import subprocess
from std_msgs.msg import UInt16
from std_msgs.msg import String


def callback(kinect_data):
    check_Map1 = 'A1'
    check_Map2 = 'A2'
    
    cmd_Map1 = "roslaunch 'navstack_pub' 'switch_map_trial.launch' "
    cmd_Map2 = "roslaunch 'navstack_pub' 'switch_map2_trial.launch' "
    
    if(check_Map1 == kinect_data.data):
        #subprocess.call(cmd_Map1, shell=True)
        print(kinect_data.data) 
        
    elif(check_Map2 == kinect_data.data):
        subprocess.call(cmd_Map2, shell=True) 
               
    print(kinect_data.data) 
    


rospy.init_node("subscriber")
rospy.Subscriber("barcode",String,callback)
rospy.spin()

