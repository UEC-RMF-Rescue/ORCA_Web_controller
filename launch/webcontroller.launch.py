from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration, PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import AnyLaunchDescriptionSource
import os
import time


def generate_launch_description():
    # file name and path
    web_controller_pkg_name = "orca_web_controller"

    # web bridge
    bridge = IncludeLaunchDescription(
        AnyLaunchDescriptionSource(
            PathJoinSubstitution([
                FindPackageShare('rosbridge_server'),
                'launch',
                'rosbridge_websocket_launch.xml',
            ])
        )
    )
    
    server = ExecuteProcess(
        cmd=[
            'python3', '-m', 'http.server', '8000',
            '--directory', os.path.join(get_package_share_directory(web_controller_pkg_name), 'web_interface')
        ],
        output = "screen",
    )

    return LaunchDescription([
        bridge,
        server,
    ])
