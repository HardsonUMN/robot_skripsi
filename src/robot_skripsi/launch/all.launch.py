from launch import LaunchDescription
import launch_ros.actions
from getkey import getkey, keys

def generate_launch_description():
    return LaunchDescription([
        launch_ros.actions.Node(
            package = 'robot_skripsi', executable= 'Str_coms_client'),
        launch_ros.actions.Node(
            package = 'robot_skripsi', executable = 'Str_pico0_server'),
        #launch_ros.actions.Node(
            #package = 'robot_skripsi', executable = 'Str_pico1_server'),
        launch_ros.actions.Node(
            package = 'robot_skripsi', executable = 'teleop_key_move')
                
    ])

    # return LaunchDescription([
    #     launch_ros.actions.Node(
    #         package = 'tempest_robot', executable= 'nano0_server'),
    #     launch_ros.actions.Node(
    #         package = 'tempest_robot', executable = 'nano1_server'),
    #     launch_ros.actions.Node(
    #         package = 'tempest_robot', executable = 'sending_angle'),
    # ])