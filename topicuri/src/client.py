#!/usr/bin/env python3
import rospy
from topicuri.srv import CustomServMess

Ionita_Redenciuc = "Ionita_Redenciuc"

def triangle_client():
    rospy.init_node('triangle_client')
    side = rospy.get_param('~side', 1.5)
    repetitions = rospy.get_param('~repetitions', 1)

    rospy.wait_for_service('make_triangle')
    try:
        make_triangle = rospy.ServiceProxy('make_triangle', CustomServMess)
        rospy.loginfo(f"[{Ionita_Redenciuc}] serere servicu make_triangle: side={side}, repetitions={repetitions}")
        raspuns = make_triangle(side, repetitions)

        if raspuns.success:
            rospy.loginfo(f"[{Ionita_Redenciuc}] triunghi complet")
        else:
            rospy.logwarn(f"[{Ionita_Redenciuc}] service returned success=False.")

    except rospy.ServiceException as e:
        rospy.logerr(f"[{Ionita_Redenciuc}] eroare serviciu: {e}")

if __name__ == '__main__':
    triangle_client()