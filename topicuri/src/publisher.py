#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidance:
    def __init__(self):
        rospy.init_node('obstacle_avoidance')

        self.pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
        self.sub = rospy.Subscriber('/scan', LaserScan, self.callback)
        self.cmd = Twist()

    def callback(self, msg):
       
        front_distance = min(min(msg.ranges[0:10]), min(msg.ranges[-10:]))

        if front_distance < 0.5:
            self.cmd.linear.x = 0.0
            self.cmd.angular.z = 0.5
        else:
            self.cmd.linear.x = 0.2
            self.cmd.angular.z = 0.0

        self.pub.publish(self.cmd)

    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = ObstacleAvoidance()
    node.run()