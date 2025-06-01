cmake_minimum_required(VERSION 3.5)
project(orca_web_controller)

find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  orca_web_controller/orca_web_controller.py
  DESTINATION lib/${PROJECT_NAME}
)

rosidl_target_interfaces(${PROJECT_NAME}
  ${PROJECT_NAME}
  INTERFACE
)

ament_package()
