#! /usr/bin/env python3

"""
Description:
    This ROS2 node periodically publihes "Hello world" message to a topic.

-----
Publishing Topics:
    The channel containing the "Hello World" messages
    /py_example_topic - std_msgs/String

Subscription Topics:
    None
-----
Author: Raj Srikanth
Date: July 29, 2025
"""

import rclpy  # import the ROS2 client library for python
from rclpy.node import Node  # import the node class, used for creating nodes

from std_msgs.msg import String  # import string message type for ROS2


class minpypub(Node):
    """Create a min publisher node

    """

    def __init__(self):
        super().__init__('min_py_pub')

        self.publisher_1 = self.create_publisher(String, '/py_example_topic', 10)

        timer_period = 0.5
        self.timer = self.create_timer(timer_period, self.timer_callback)

        self.i = 0

    def timer_callback(self):
        msg = String()

        msg.data = 'Hello World: %d' % self.i

        self.publisher_1.publish(msg)

        self.get_logger().info('Publishing: "%s"' % msg.data)

        self.i = self.i + 1


def main(args=None):
    """Main function torun the ROS2 code
    """
    rclpy.init(args=args)
    min_py_pub = minpypub()

    rclpy.spin(min_py_pub)

    min_py_pub.destroy_node

    rclpy.shutdown()


if __name__ == '__main__':
    main()
