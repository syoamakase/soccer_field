#!/usr/bin/env python

import sys

import rospy
from geometry_msgs.msg import Twist


class Control:
    def __init__(self, robot_name="mobile_base"):
        topic_name = robot_name+'/commands/velocity'
        rospy.init_node(robot_name+'_vel_publisher')
        self.pub = rospy.Publisher(topic_name, Twist, queue_size=10)


    def move_action(self,acition):
        vel = Twist()
        self.move_to_neutral()
        self.move_forward()


    def move_to_neutral(self):
        vel = Twist()
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        self.pub.publish(vel)
        rospy.sleep(1.0)

    def move_forward(self):
        vel = Twist()
        vel.linear.x = 1.0
        self.pub.publish(vel)
        rospy.sleep(7.0)


def main():
    control = Control()
    control.move_action(1)
    rospy.spin()


if __name__ == "__main__":
    sys.exit(main())    
