from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
import os
from ament_index_python.packages import get_package_share_directory
import xacro

def generate_launch_description():
    pkg_name = 'amr_pkg'
    
    # Absolute path to your .xacro file
    xacro_file = os.path.join(
        get_package_share_directory(pkg_name),
        'description',
        'final.urdf.xacro'
    )

    # Run xacro to generate robot_description
    doc = xacro.process_file(xacro_file)
    robot_desc = doc.toxml()


    return LaunchDescription([
    
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{
                'robot_description': robot_desc,
                'use_sim_time': True
            }]
        ),
    ])
