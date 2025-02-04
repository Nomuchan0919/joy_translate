#ファイル名　joy_translate_node.py
import rclpy
from rclpy.node import Node #Nodeクラス
from std_msgs.msg import String #Stringメッセージ型
from geometry_msgs.msg import Twist #Twistメッセージ型　亀用
from sensor_msgs.msg import Joy #Joy

class JoyTranslate(Node): #publisherクラス
    def __init__(self):
        super().__init__('joy_translate_pub_node') #ノード名
        self.publisher = self.create_publisher(Twist, '/turtle1/cmd_vel', 10) #第3引数はキューの上限
        self.subscription = self.create_subscription(Joy, 'joy', self.listener_callback, 10)
        self.vel = Twist()

    def listener_callback(self, joy): #subscribeするたびに呼ばれる
        self.vel.linear.x = joy.axes[1] #linearのxに左スティックの前後を入れる。
        self.vel.angular.z =joy.axes[3] #angularのzに右スティックの左右を入れる。
        self.publisher.publish(self.vel)
        self.get_logger().info("Velocity: Linear=%f angular=%f" % (self.vel.linear.x, self.vel.angular.z))

def main(args=None):
    rclpy.init(args=args) #rclpyの初期化
    joy_translate = JoyTranslate()
    rclpy.spin(joy_translate)
    rclpy.shutdown()

if __name__ == '__main__':
    main()