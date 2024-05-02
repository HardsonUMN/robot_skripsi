#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from robot_interfaces.action import SendStr
from rclpy.action import ActionClient
from rclpy.action.client import ClientGoalHandle 

from std_msgs.msg import String
from time import sleep

class SendStrPico0ClientNode(Node):

    def __init__(self):
        super().__init__("Str_coms_client")
        self.subscriber_move = self.create_subscription(String, "/state", self.send_goal, 1)
        self.Str_pico0_client_ = ActionClient(
            self, SendStr, "Str_pico0")
        #self.Str_pico1_client_ = ActionClient(
            #self, SendStr, "Str_pico1")
        self.get_logger().info("Action Client has been started")

    def send_goal(self, message:String):
        #wait for server
        self.Str_pico0_client_.wait_for_server()

        #create goal0
        goal = SendStr.Goal()
        goal.target_movement = message.data

        #send the goal0
        self.get_logger().info("sending goal0")
        self.Str_pico0_client_.send_goal_async(goal).add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        self.goal_handle_: ClientGoalHandle = future.result()
        if self.goal_handle_.accepted:
            self.goal_handle_.get_result_async().add_done_callback(self.goal_result_callback)

    def goal_result_callback(self, future):
        #result = future.result().result
        #self.get_logger().info("Result: " + str(result.reached_movement))

        """self.Str_pico1_client_.wait_for_server()
        #create goal1
        goal = SendStr.Goal()
        result = future.result().result
        goal.target_movement = result.reached_movement
        #send the goal1
        self.get_logger().info("sending goal1")
        self.Str_pico1_client_.send_goal_async(goal)"""

def main (args=None):
    rclpy.init(args=args)
    node = SendStrPico0ClientNode()
    node.send_goal("maju")
    rclpy.spin(node)
    rclpy.shutdown

if __name__ == '__main__':
    main()