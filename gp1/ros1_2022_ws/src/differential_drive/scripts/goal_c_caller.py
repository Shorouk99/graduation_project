#!/usr/bin/env python
import  rospy
from std_msgs.msg import Bool

rospy.init_node("goal_caller")
pub = rospy.Publisher("goal_elev_request", Bool, queue_size=10)

pub.publish(True)
rospy.sleep(10)

rospy.spin()
