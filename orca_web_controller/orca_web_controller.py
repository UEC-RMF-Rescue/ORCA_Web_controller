import rclpy
from rclpy.node import Node
from std_msgs.msg import Bool
from std_srvs.srv import Empty

class OrcaWebController(Node):
    def __init__(self):
        super().__init__('orca_web_controller')

        # Publisher（Webから受け取って処理したいならsubscriberも必要）
        self.pub = self.create_publisher(Bool, 'is_manual', 10)
        self.sub = self.create_subscription(Bool, 'is_manual', self.is_manual_callback, 10)

        # Services
        self.set_offset_srv = self.create_service(Empty, 'set_offset', self.handle_set_offset)
        self.is_enable_srv = self.create_service(Empty, 'is_enable', self.handle_is_enable)

        self.enabled = False

    def handle_set_offset(self, request, response):
        self.get_logger().info('offset is called')
        return response

    def handle_is_enable(self, request, response):
        self.get_logger().info('isEnable is called')
        return response

    def is_manual_callback(self, msg):
        self.get_logger().info(f'Received is_manual: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = OrcaWebController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
