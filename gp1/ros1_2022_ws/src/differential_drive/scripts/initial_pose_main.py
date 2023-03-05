#!/usr/bin/env python
import  rospy
from geometry_msgs.msg import PoseWithCovarianceStamped


rospy.init_node('initial_pos_main', anonymous=True)

pub = rospy.Publisher('/initialpose', PoseWithCovarianceStamped, queue_size=1)
initialpose_msg = PoseWithCovarianceStamped()
initialpose_msg.header.frame_id="map"
initialpose_msg.pose.pose.position.x = 17.9648170471
initialpose_msg.pose.pose.position.y = 3.29979991913
#initialpose_msg.pose.pose.orientation.z = -0.707109578327
initialpose_msg.pose.pose.orientation.w = 0.741181321798	
#rate = rospy.Rate(1)


while pub.get_num_connections()<1:
    pass
pub.publish(initialpose_msg)
     #rate.sleep()
   
