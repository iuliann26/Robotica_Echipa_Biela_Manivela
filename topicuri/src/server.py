#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
from topicuri.srv import CustomServMess, CustomServMessResponse

Ionita_Redenciuc = "Ionita_Redenciuc"


def stop_robot(pub):
    stop_cmd = Twist()
    pub.publish(stop_cmd)
    rospy.sleep(0.2)


def move(pub, linear_speed, angular_speed, duration):
    cmd = Twist()
    cmd.linear.x = linear_speed
    cmd.angular.z = angular_speed
    end_time = rospy.Time.now() + rospy.Duration(duration)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown() and rospy.Time.now() < end_time:
        pub.publish(cmd)
        rate.sleep()
    stop_robot(pub)


def drive_triangle(pub, side, repetitions):
    linear_speed = 0.25
    angular_speed = 0.5
    forward_time = abs(side) / linear_speed
    turn_time = (2.0 * 3.141592653589793 / 3.0) / angular_speed

    for repeat in range(repetitions):
        rospy.loginfo(f"[{Ionita_Redenciuc}] Repetitia {repeat + 1}/{repetitions}: incep triunghi")
        for edge in range(3):
            rospy.loginfo(f"[{Ionita_Redenciuc}] Latura {edge + 1}/3: merg inainte {side} metri")
            move(pub, linear_speed if side >= 0 else -linear_speed, 0.0, forward_time)
            rospy.loginfo(f"[{Ionita_Redenciuc}] ")
            move(pub, 0.0, angular_speed, turn_time)


def handle_triangle(req):
    rospy.loginfo(f"[{Ionita_Redenciuc}] am primit cererea: side={req.side}, repetitions={req.repetitions}")
    cmd_vel_topic = rospy.get_param('~cmd_vel_topic', '/cmd_vel')
    pub = rospy.Publisher(cmd_vel_topic, Twist, queue_size=10)
    rospy.sleep(1.0)
    drive_triangle(pub, req.side, req.repetitions)
    stop_robot(pub)
    return CustomServMessResponse(success=True)


if __name__ == '__main__':
    rospy.init_node('triangle_server')
    rospy.Service('make_triangle', CustomServMess, handle_triangle)
    rospy.loginfo(f"[{Ionita_Redenciuc}] se asteapta cereri:")
    rospy.spin()