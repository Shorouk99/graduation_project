import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan

class OdomNode(Node):

    def __init__(self):
        super().__init__('odom_node') # Call Node constructor and give the node the name "odom_node"
        self.scan_pub = self.create_publisher(LaserScan, '/scan/new', 10)
        # timer_period = 0.1  # seconds
        # self.timer = self.create_timer(timer_period, self.timer_callback)

        # self.encoder_counts = 0

        self.subscription = self.create_subscription(
            LaserScan,
            '/scan',
            self.listener_callback,
            10)
        self.subscription



    def listener_callback(self, msg):
        self.scan_pub.publish(msg)
        self.get_logger().info('distance =  "%s"' % msg.ranges)



    # def timer_callback(self):
    # 	# dist = ((float(self.encoder_counts)/1080.0)*2.0*3.14*0.06)
    #     dist = Float64()
    #     dist.data = (float(self.encoder_counts)/1080.0)*2.0*3.14*0.06
    #     self.odom_pub.publish(dist)
    #     self.get_logger().info('distance =  "%s"' % dist.data)


def main(args=None):
    rclpy.init(args=args)

    odom_node = OdomNode()

    rclpy.spin(odom_node)

    # minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()