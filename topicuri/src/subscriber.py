#!/usr/bin/env python
import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def callback(msg):
    num = len(msg.ranges)
    
    fata = msg.ranges[num // 2]
    dreapta = msg.ranges[0]
    stanga = msg.ranges[num - 1]

    move = Twist()

    
    if fata > 1.0:
        move.linear.x = 0.2
    elif fata < 1.0 or dreapta < 1.0:
        move.angular.z = 0.5  
    elif stanga < 1.0:
        move.angular.z = -0.5 # 

    
    pub.publish(move)

rospy.init_node('subscriber')
sub = rospy.Subscriber('/scan', LaserScan, callback)
pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

rospy.spin()