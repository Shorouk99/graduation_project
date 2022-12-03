# Author: Shorouk Magdy
# shorouk.magdy.anwar@gmail.com
# Date: December 1, 2022
# Description: This script publishes twist msgs to /cmd_vel topic

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)


    def timer_callback(self):

        # publishing simulated cmd_vel data
        v_msg = Twist(linear=Vector3(x=0.0, y=0.0, z=0.0), angular=Vector3(x=0.0, y=0.0, z=0.0))
        self.vel_pub.publish(v_msg)
        self.get_logger().info('Publishing: "%s"' % v_msg)


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()