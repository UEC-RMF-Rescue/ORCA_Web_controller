import rclpy
from rclpy.node import Node
from std_srvs.srv import Empty
import asyncio
import websockets
import json


class WebSocketServiceBridge(Node):
    def __init__(self):
        super().__init__('websocket_service_bridge')
        self.set_offset_client = self.create_client(Empty, 'set_offset')
        self.is_enable_client = self.create_client(Empty, 'is_enable')

    async def handle_ws(self, websocket, path):
        async for message in websocket:
            data = json.loads(message)

            if data.get("type") == "call_service":
                service = data.get("service")

                if service == "set_offset":
                    await self.call_empty_service(websocket, self.set_offset_client, "set_offset")
                elif service == "is_enable":
                    await self.call_empty_service(websocket, self.is_enable_client, "is_enable")
                else:
                    await websocket.send("Unknown service requested.")

    async def call_empty_service(self, websocket, client, name):
        while not client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(f"Waiting for {name} service...")

        req = Empty.Request()
        future = client.call_async(req)
        rclpy.spin_until_future_complete(self, future)

        if future.result() is not None:
            await websocket.send(f"{name} called successfully.")
        else:
            await websocket.send(f"{name} call failed.")


async def main_async():
    rclpy.init()
    node = WebSocketServiceBridge()
    async def handler(websocket, path):
        await node.handle_ws(websocket, path)

    server = await websockets.serve(handler, "0.0.0.0", 8765)

    loop = asyncio.get_running_loop()
    await loop.run_in_executor(None, lambda: rclpy.spin(node))

    server.close()
    await server.wait_closed()
    node.destroy_node()
    rclpy.shutdown()


def main():
    asyncio.run(main_async())


if __name__ == "__main__":
    main()
