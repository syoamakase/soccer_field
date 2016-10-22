#!/usr/bin/env python
import rospy
from std_msgs.msg import String 
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Twist 

def callback(message):
    for i in range(len(message.name)):
        if message.name[i] == 'robocup_3Dsim_ball':
            print(message.pose[i])

rospy.init_node('pose_object')

sub = rospy.Subscriber('/gazebo/model_states', ModelStates, callback)
rospy.spin()
