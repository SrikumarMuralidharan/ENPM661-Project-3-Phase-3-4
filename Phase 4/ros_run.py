#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from maze import Map
from robot import Robot

def read_file():
    file = open('/home/srikumar/sriku_ws/src/astar_imp/src/action.txt', "r")
    c = []
    lines = file.readlines()
    for i, line in enumerate(lines):
        a=float(line.split(',')[0])
        b=float(line.split(',')[-1])
        c.append((a,b))
    return c

#ros commands
rospy.init_node('ros_run', anonymous=True)
velPub = rospy.Publisher('cmd_vel', Twist, queue_size=100)
msg = Twist()

turtlebot3_model = rospy.get_param("model", "burger")


msg.linear.x = 0.0
msg.linear.y = 0.0
msg.linear.z = 0.0
msg.angular.x = 0.0
msg.angular.y = 0.0
msg.angular.z = 0.0

velPub.publish(msg)

mymap = Map()

mymap.GetUserNodes()

robot = Robot(mymap)

ros=[]
action_set = read_file()
for action in action_set:
    ros.append(action)
print(ros)
c =0
r = rospy.Rate(10)
for action in ros:
    print("action")
    print(action)

    while not rospy.is_shutdown():
        if c== 101:
            msg.linear.x = 0
            msg.angular.z = 0
            velPub.publish(msg)
            break
        else:
            vel, th = robot.ros_act(action[0],action[1])
            msg.linear.x = vel*80
            msg.angular.z =  th*50
            velPub.publish(msg)
            c=c+1
            r.sleep()
    c=0
