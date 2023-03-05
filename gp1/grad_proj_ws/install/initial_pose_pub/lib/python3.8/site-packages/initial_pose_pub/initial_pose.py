import rclpy
from rclpy.node import Node
from geometry_msgs.msg import PoseWithCovarianceStamped

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.initialpose_pub = self.create_publisher(PoseWithCovarianceStamped, '/initialpose', 10)
        timer_period = 0.1  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    # def timer_callback(self):
    # 	self.i = self.i + 1 
    # 	if self.i == 70:
	#         initialpose_msg = PoseWithCovarianceStamped()
    #         initialpose_msg.header.frame_id='map'
    #         initialpose_msg.pose.pose.position.x=5.327165126800537
    #         initialpose_msg.pose.pose.position.y=-8.965409278869629
	#         initialpose_msg.pose.pose.orientation.w=1.0
	#         self.initialpose_pub.publish(initialpose_msg)
	#         self.get_logger().info('Publishing: "%s"' % initialpose_msg)  
	#         self.destroy_node()

    def timer_callback(self):
        self.i = self.i+1
        if self.i == 70:
            initialpose_msg = PoseWithCovarianceStamped()
            initialpose_msg.header.frame_id='map'
            # initialpose_msg.pose.pose.position.x = 5.2078728675842285
            # initialpose_msg.pose.pose.position.y = -7.894547462463379
            initialpose_msg.pose.pose.position.x = 0.0
            initialpose_msg.pose.pose.position.y = 0.0
            initialpose_msg.pose.pose.orientation.x = 0.0
            initialpose_msg.pose.pose.orientation.y=0.0
            initialpose_msg.pose.pose.orientation.z=0.0
            initialpose_msg.pose.pose.orientation.w = 1.0
            self.initialpose_pub.publish(initialpose_msg)
            self.get_logger().info('Publishing: "%s"' % initialpose_msg)
            self.destroy_node()


def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()