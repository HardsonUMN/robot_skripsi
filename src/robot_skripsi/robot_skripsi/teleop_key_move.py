import rclpy
from rclpy.node import Node
from getkey import getkey, keys
from std_msgs.msg import String
import time

def tahan_waktu(waktu):
    flag = True
    myTime = time.time()
    while flag == True:
        currentTime = time.time()
        if currentTime - myTime < waktu:
            flag = True
        elif currentTime - myTime >= waktu:
            flag = False
    

class TeleopKeyNode(Node):
    def __init__(self):
        super().__init__("teleop_key_move")
        self.talking_one = self.create_publisher(String, "/state", 1)

        self.timer_ = self.create_timer(0.1, self.send_message)
        self.get_logger().info("W (Maju) | A (Menghadap Kiri) | S (Capit) | D (Menghadap Kanan)| X (Mundur)")
        
    def send_message(self):
        # if GPIO.input(GPIO.BUTTON)==1:
        #     self.get_logger().info("Aktif")
        key = getkey()
        message = String()
        if key == 'w':
            self.get_logger().info("Maju")
            message.data = "-Maju-"
            self.talking_one.publish(message)
        elif key == 's':
            self.get_logger().info("Mundur")
            message.data = "-mundur-"
            self.talking_one.publish(message)
        elif key == 'd':
            self.get_logger().info("Menghadap Kanan")
            message.data = "-kanan-"
            self.talking_one.publish(message)
        elif key == 'a':
            self.get_logger().info("Menghadap Kiri")
            message.data = "-kiri-"
            self.talking_one.publish(message)
        elif key == 'f':
            self.get_logger().info("Berdiri")
            message.data = "-stop-"
            self.talking_one.publish(message)

        else:
            self.get_logger().info("Wrong Key")

def main(args=None):
    rclpy.init(args=args)
    node = TeleopKeyNode()
    rclpy.spin(node)
    rclpy.shutdown()