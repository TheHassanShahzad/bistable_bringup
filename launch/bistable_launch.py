from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    # Nodes which we want to launch
    gamepad_publisher_node =  Node(   # "gamepad_publisher_node" is a node object local to this file no the name is irrelevant
        package="BiStable_scripts",       # replace with whatever you named your package (Bistable_scripts?)
        executable="gamepad_publisher" # this too. Same for below. Then you can colcon build.
    )
    # RENAME <exec_depend>bistable_pkg</exec_depend> to whatever you called it in the package.xml file!!!!!!!!!!!

    tracking_publisher_node =  Node(
        package="BiStable_scripts",   
        executable="tracking_publisher" 
    )

    combiner_node =  Node(
        package="BiStable_scripts",   
        executable="combiner_node" 
    )

    #micro_ros_agent_node = Node(
    #     package="micro_ros_agent",
    #     executable="micro_ros_agent",
    #     arguments=[
    #         'serial',
    #         '--dev',
    #         '/dev/tty/USB0'
    #     ]
    # )

    # Launch nodes
    ld.add_action(gamepad_publisher_node)
    ld.add_action(combiner_node)
    ld.add_action(tracking_publisher_node) 
    #ld.add_action(micro_ros_agent_node)
    return ld
