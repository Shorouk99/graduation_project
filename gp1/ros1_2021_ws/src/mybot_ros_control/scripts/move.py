#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import PoseStamped

rospy.init_node("Publisher_node")
pub = rospy.Publisher("/twist", Twist, queue_size=10)
#pub = rospy.Publisher("/move_base_simple/goal", PoseStamped, queue_size=1)

goal = PoseStamped()
vel = Twist()

while not rospy.is_shutdown():
	goal.pose.position.x = 1;
	goal.pose.position.y = 0;
	vel.linear.x = 10
	vel.linear.y = 0
	vel.linear.z = 0
	vel.angular.x = 0
	vel.angular.y = 0
	vel.angular.z = 0
	pub.publish(vel)
	#pub.publish(goal)
	rospy.sleep(1)
