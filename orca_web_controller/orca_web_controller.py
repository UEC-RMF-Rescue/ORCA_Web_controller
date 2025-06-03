import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Bool
from std_srvs.srv import Empty

class OrcaWebController(Node):
    def __init__(self):
        super().__init__('orca_web_controller')

        # Publisher
        self.state_pub = self.create_publisher(Int32, '/orca_00/control_state', 10)
        self.enabled_state_pub = self.create_publisher(Bool, '/orca_00/enabled_state', 10)

        # Services
        self.set_offset_srv = self.create_service(Empty, '/orca_00/set_offset', self.handle_set_offset)
        self.enable_srv = self.create_service(Empty, '/orca_00/enable', self.handle_enable)
        self.disable_srv = self.create_service(Empty, '/orca_00/disenable', self.handle_disable)

        self.enabled = False

    def handle_set_offset(self, request, response):
        self.get_logger().info('orca_00 : offset is called')
        return response

    def handle_enable(self, request, response):
        self.enabled = True
        self.get_logger().info('orca_00  : enabled')
        self.enabled_state_pub.publish(Bool(data=True))
        return response

    def handle_disable(self, request, response):
        self.enabled = False
        self.get_logger().info('orca_00  : disabled')
        self.enabled_state_pub.publish(Bool(data=False))
        return response

def main(args=None):
    rclpy.init(args=args)
    node = OrcaWebController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
