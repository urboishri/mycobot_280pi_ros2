cmake_minimum_required(VERSION 3.8)
project(mycobot_280pi_description)

# This package has NO C++ code.
# ament_cmake only needs itself — everything else is exec_depend in package.xml
find_package(ament_cmake REQUIRED)

# Install all resource directories into the share folder so ROS 2 can find
# our URDF, meshes, and launch files via get_package_share_directory()
install(
  DIRECTORY urdf meshes launch rviz
  DESTINATION share/${PROJECT_NAME}
)

ament_package()
