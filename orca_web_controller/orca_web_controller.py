import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32, Bool
from std_srvs.srv import Empty
from rclpy.executors import MultiThreadedExecutor

class OrcaWebController(Node):
    def __init__(self, robot_name='orca_00'):
        super().__init__(f'{robot_name}_web_controller')
        self.robot_name = robot_name

        self.state_pub = self.create_publisher(Int32, f'/{robot_name}/control_state', 10)
        self.enabled_state_pub = self.create_publisher(Bool, f'/{robot_name}/enabled_state', 10)

        self.set_offset_srv = self.create_service(Empty, f'/{robot_name}/set_offset', self.handle_set_offset)
        self.enable_srv = self.create_service(Empty, f'/{robot_name}/enable', self.handle_enable)
        self.disable_srv = self.create_service(Empty, f'/{robot_name}/disable', self.handle_disable)

        self.enabled = False

    def handle_set_offset(self, request, response):
        self.get_logger().info(f'{self.robot_name} : offset is called')
        return response

    def handle_enable(self, request, response):
        self.enabled = True
        self.get_logger().info(f'{self.robot_name} : enabled')
        self.enabled_state_pub.publish(Bool(data=True))
        return response

    def handle_disable(self, request, response):
        self.enabled = False
        self.get_logger().info(f'{self.robot_name} : disabled')
        self.enabled_state_pub.publish(Bool(data=False))
        return response

def main(args=None):
    rclpy.init(args=args)

    # 複数ロボット用ノードを作成
    robot_names = ['orca_00', 'orca_01', 'orca_02']
    nodes = [OrcaWebController(name) for name in robot_names]

    # マルチスレッドでノードを実行
    executor = MultiThreadedExecutor()
    for node in nodes:
        executor.add_node(node)

    try:
        executor.spin()
    finally:
        for node in nodes:
            node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()