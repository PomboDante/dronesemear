#!/usr/bin/env python
#codigo relativo ao sistema de mov. robo vermelho(imcompleto)
import rospy
from geometry_msgs.msg import Twist
import random
import time

def move_and_turn():
    rospy.init_node('move_and_turn', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(10)  # 10 Hz
    move_cmd = Twist()

    
    move_cmd.linear.x = 0.5  
    move_cmd.angular.z = 0.0  
    start_time = time.time()
    while time.time() - start_time < 5:
        pub.publish(move_cmd)
        rate.sleep()

   
    move_cmd.linear.x = 0.0
    pub.publish(move_cmd)
    rospy.sleep(1) 

    
    direction = random.choice(['left', 'right'])
    if direction == 'left':
        move_cmd.angular.z = 0.5 
    else:
        move_cmd.angular.z = -0.5  

    
    start_time = time.time()
    while time.time() - start_time < 2:
        pub.publish(move_cmd)
        rate.sleep()

    
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)

if __name__ == '__main__':
    try:
        move_and_turn()
    except rospy.ROSInterruptException:
        pass
