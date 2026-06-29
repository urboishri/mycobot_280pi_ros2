import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import Command
from launch_ros.parameter_descriptions import ParameterValue
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg_path = get_package_share_directory('mycobot_280pi_description')
    urdf_file = os.path.join(pkg_path, 'urdf', 'mycobot_280pi.urdf.xacro')
    rviz_config = os.path.join(pkg_path, 'rviz', 'mycobot_280pi.rviz')

    # ParameterValue(..., value_type=str) tells Humble explicitly:
    # "this is a string, don't try to parse it as YAML"
    # This is required in Humble but not needed in Jazzy/Iron (they fixed it)
    robot_description = {
        'robot_description': ParameterValue(
            Command(['xacro ', urdf_file]),
            value_type=str
        )
    }

    return LaunchDescription([

        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[robot_description],
            output='screen'
        ),

        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            output='screen'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            output='screen',
            arguments=['-d', rviz_config] if os.path.exists(rviz_config) else []
        ),

    ])
