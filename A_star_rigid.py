from sys import exit
from maze import Map
from robot import Robot

write_to_video = True
show_visualization = True

mymap = Map()

mymap.GetUserNodes()

# Construct the robot
robot = Robot(mymap)

robot.A_Star()

if robot.foundGoal:
    robot.backtrack_path()
else:
    print('The goal could not be found')
    exit()
# Visualize the path
robot.visualize(write_to_video,show_visualization)