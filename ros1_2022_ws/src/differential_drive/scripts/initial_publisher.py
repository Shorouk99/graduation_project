#!/usr/bin/env python
import  rospy
import subprocess
from std_msgs.msg import UInt16
from std_msgs.msg import String

																		
def callback(kinect_data):
    check_Map1 = 'A1'
    check_Map2 = 'A2'
    
    cmd_Map1 = "rosrun 'initial_pose_publisher' 'initial_pose_publisher_node' "
    
    if(check_Map2 == kinect_data.data):
        subprocess.call(cmd_Map1, shell=True) 
        print(kinect_data.data) 


               
    print(kinect_data.data) 
    


rospy.init_node("sub")
rospy.Subscriber("barcode",String,callback)
rospy.spin()

