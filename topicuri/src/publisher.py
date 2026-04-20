#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def ionita_redenciuc():
    rospy.init_node('publisher')
    
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        move = Twist()
        
        pub.publish(move)
        rate.sleep()

if __name__ == '__main__':
    try:
        ionita_redenciuc()
    except rospy.ROSInterruptException:
        pass