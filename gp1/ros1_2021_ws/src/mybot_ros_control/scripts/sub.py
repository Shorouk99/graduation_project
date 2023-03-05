#!/usr/bin/env python
import rospy 
from geometry_msgs.msg import Twist

def callback(right_msg):
	print("Right Ticks = {}".format(right_msg.angular.z))


def callback1(left_msg):
	print("Left Ticks = {}".format(left_msg.angular.z))


rospy.init_node("subscriber")
sub1 = rospy.Subscriber("/right_vel", Twist, callback)
sub2 = rospy.Subscriber("/left_vel", Twist, callback1)

rospy.spin()
