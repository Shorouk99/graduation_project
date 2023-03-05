import rclpy
from rclpy.node import Node
# from std_msgs.msg import Float64
from sensor_msgs.msg import Imu
from geometry_msgs.msg import Vector3
import math

class QuatToEuler(Node):
	def __init__(self):
		super().__init__('quat_to_euler')
		self.euler_publisher = self.create_publisher(Vector3, '/euler/ypr', 10)
		timer_period = 0.1
		self.timer = self.create_timer(timer_period, self.timer_callback)

		self.subscription = self.create_subscription(Imu, '/imu/data', self.listener_callback, 10)
		self.subscription

		self.x = 0
		self.y = 0
		self.z = 0
		self.w = 1

	def listener_callback(self, msg):
		self.x = msg.orientation.x
		self.y = msg.orientation.y
		self.z = msg.orientation.z
		self.w = msg.orientation.w

	def timer_callback(self):
		t0 = +2.0 * (self.w * self.x + self.y * self.z)
		t1 = +1.0 - 2.0 * (self.x * self.x + self.y * self.y)
		roll_x = math.atan2(t0, t1)
		roll_x = roll_x * 57.2958

		t2 = +2.0 * (self.w * self.y - self.z * self.x)
		t2 = +1.0 if t2 > +1.0 else t2
		t2 = -1.0 if t2 < -1.0 else t2
		pitch_y = math.asin(t2)
		pitch_y = pitch_y * 57.2958

		t3 = +2.0 * (self.w * self.z + self.x * self.y)
		t4 = +1.0 - 2.0 * (self.y * self.y + self.z * self.z)
		yaw_z = math.atan2(t3, t4)
		yaw_z = yaw_z * 57.2958

		ypr = Vector3(x= roll_x, y=pitch_y, z=yaw_z)
		self.euler_publisher.publish(ypr)
		self.get_logger().info('\nypr =  "%s"' % ypr)


def main(args=None):
    rclpy.init(args=args)

    ypr_node = QuatToEuler()

    rclpy.spin(ypr_node)

    rclpy.shutdown()


if __name__ == '__main__':
    main()





