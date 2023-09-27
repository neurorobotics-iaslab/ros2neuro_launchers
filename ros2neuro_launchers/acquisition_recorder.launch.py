import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

   return LaunchDescription([
      Node(
         package='ros2neuro_acquisition',
         executable='acquisition',
         parameters=[
            {"plugin" : "ros2neuro::EGDDevice"},
            {"framerate" : 16.0},
            {"devarg" : "/home/paolo/prova16ch.gdf"},
            {"samplerate" : 512}
         ]
      ),
      Node(
         package='ros2neuro_recorder',
         executable='recorder',
         parameters=[
            {"autostart" : True},
            {"filename" : ""},
            {"protocol/subject" : "c7"},
            {"protocol/modality" : "bhbf"}
         ]
      )
   ])