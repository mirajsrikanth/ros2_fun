#! /usr/bin/env python3

"""
Description:
    Thi ROS2 node subscribes to "Hello World" messages.
--------
Publishing Topics:
    None
--------
Subscription Topics:
    The channel containing the "Hello World" messages
    /py_example_topic - std_msgs/String

--------
Author: Ra Srikanth
Date: Aug 2, 2025
"""
import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class minpysub(Node):
    def __init__(self):
        super().__init__('min_py_sub')

        self.subscriber_1 = self.create_subscription(
            String,
            'py_example_topic',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        self.get_logger().info(f'I heard: "{msg.data}"')


def main(args=None):
    rclpy.init(args=args)

    min_py_sub = minpysub()

    rclpy.spin(min_py_sub)

    min_py_sub.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
