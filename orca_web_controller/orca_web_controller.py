import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_srvs.srv import Empty

class OrcaWebController(Node):
    def __init__(self):
        super().__init__('orca_web_controller')

        # Publisher（Webから受け取って処理したいならsubscriberも必要）
        self.pub = self.create_publisher(Int32, '/orca_00/control_state', 10)

        # Services
        self.set_offset_srv = self.create_service(Empty, '/orca_00/set_offset', self.handle_set_offset)
        self.enable_srv = self.create_service(Empty, '/orca_00/enable', self.handle_enable)
        self.disable_srv = self.create_service(Empty, '/orca_00/disenable', self.handle_enable)
        

        self.enabled = False

    def handle_set_offset(self, request, response):
        self.get_logger().info('orca_00 : offset is called')
        return response

    def handle_enable(self, request, response):
        self.get_logger().info('orca_00 enabled')
        return response

def main(args=None):
    rclpy.init(args=args)
    node = OrcaWebController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
