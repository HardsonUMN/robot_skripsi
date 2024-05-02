#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from robot_interfaces.action import SendStr
from rclpy.action import ActionServer
from rclpy.action.server import ServerGoalHandle

from std_msgs.msg import String
import time
import serial

flag = True
ser = serial.Serial('/dev/ttyACM0', 115200, timeout=1)
myTime = time.time()
while(flag == True):
    if(time.time() - myTime < 2):
        flag = True
    elif(time.time() - myTime >= 2):
        flag = False

class SendStrPico0ServerNode(Node):
    def __init__(self):
        super().__init__("Str_pico0_server")
        self.Str_pico0_server_ = ActionServer(
            self, SendStr, "pico0_action", 
            execute_callback = self.execute_callback)
        self.get_logger().info("Action server pico0 has been started")

    def execute_callback(self, goal_handle: ServerGoalHandle):
        #get req from goal
        dat = String()
        target = goal_handle.request.target_movement

        #exc action
        self.get_logger().info("Executing the goal")
        ser.reset_input_buffer()
        kalimat = target
        ser.write(kalimat)
        self.get_logger().info(kalimat)
    
        #once done, set goal final state
        goal_handle.succeed()
        self.get_logger().info("Goal handle succeed")

        #and send the result
        result = SendStr.Result()
        result.reached_movement = target
        self.get_logger().info("Result sent")
        return result

def main (args=None):
    rclpy.init(args=args)
    node = SendStrPico0ServerNode()
    rclpy.spin(node)
    rclpy.shutdown

if __name__ == '__main__':
    main()