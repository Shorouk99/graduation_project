# Author: Shorouk Magdy
# shorouk.magdy.anwar@gmail.com
# Date: 30 Novenber 2022
# Description: This script publishes fake sensors data for troubleshooting and testing purposes

import rclpy
from rclpy.node import Node
from math import sin, cos, pi
import numpy as np

from std_msgs.msg import Int16
from geometry_msgs.msg import Quaternion
from std_msgs.msg import Header
from rclpy.clock import Clock
from sensor_msgs.msg import Imu
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Vector3
from geometry_msgs.msg import Twist


class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.lwheel_pub = self.create_publisher(Int16, 'lwheel', 10)
        self.rwheel_pub = self.create_publisher(Int16, 'rwheel', 10)
        self.imu_pub = self.create_publisher(Imu, 'imu/data', 10)
        self.laser_scan_pub = self.create_publisher(LaserScan, '/scan', 10)
        timer_period = 0.03  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        # self.i = 0


    def timer_callback(self):

        # publishing simulated encoder ticks
        msg = Int16()
        msg.data = 0
        self.lwheel_pub.publish(msg)
        self.rwheel_pub.publish(msg)
        # self.get_logger().info('Publishing: "%s"' % msg.data)
        # self.i = self.i+1
        
        # publishing simulated imu data
        imu_msg = Imu()
        imu_msg.header = Header(stamp = self.get_clock().now().to_msg(), frame_id = 'imu_link')
        orientation = Quaternion()
        orientation.x = 0.0000122
        orientation.y = 0.00001
        orientation.z = 0.003
        orientation.w = 0.99
        orientation_covariance = np.full((9), 0.0)
        orientation_covariance = orientation_covariance.tolist()

        imu_ang_vel = Vector3(x=0.0018, y=0.0014, z=0.00017)
        # angular_velocity_covariance = np.full((9), 0.0)
        angular_velocity_covariance = [4.0e-08, 0.0, 0.0, 0.0, 4.0e-08, 0.0, 0.0, 0.0, 4.0e-8]
        # angular_velocity_covariance = angular_velocity_covariance.tolist()

        imu_lin_acc = Vector3(x=0.02712944195552014, y=-0.00881083247811993, z=10.231021001446841)
        # linear_acceleration_covariance = np.full((9), 0.0)
        # linear_acceleration_covariance = linear_acceleration_covariance.tolist()
        linear_acceleration_covariance = [0.0029, 0.0, 0.0, 0.0, 0.0029, 0.0, 0.0, 0.0, 0.0029]

        imu_msg.orientation = orientation
        imu_msg.orientation_covariance = orientation_covariance
        imu_msg.angular_velocity = imu_ang_vel
        imu_msg.angular_velocity_covariance = angular_velocity_covariance
        imu_msg.linear_acceleration = imu_lin_acc
        imu_msg.linear_acceleration_covariance = linear_acceleration_covariance
        self.imu_pub.publish(imu_msg)
        # self.get_logger().info('Publishing: "%s"' % imu_msg.header)

        # publishing simulated laser scan
        laser_scan_msg = LaserScan()
        laser_scan_msg.header = Header(stamp = self.get_clock().now().to_msg(), frame_id = 'lidar_link')
        laser_scan_msg.angle_min = 0.0
        laser_scan_msg.angle_max = 3.140000104904175
        laser_scan_msg.angle_increment = 0.008746517822146416
        laser_scan_msg.time_increment = 0.0
        laser_scan_msg.scan_time = 0.0
        laser_scan_msg.range_min = 0.15000000596046448
        laser_scan_msg.range_max = 3.5
        ranges = np.full((360), np.inf)
        ranges = ranges.tolist()
        intensities = np.full((360), 47.0)
        intensities = intensities.tolist()
        laser_scan_msg.ranges = ranges 
        laser_scan_msg.intensities = intensities

        self.laser_scan_pub.publish(laser_scan_msg)
        # self.get_logger().info('Publishing: "%s"' % laser_scan_msg.header)



def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()