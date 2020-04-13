#!/usr/bin/env python

from sys import exit
from maze import Map
from robot import Robot

def read_file():
    file = open('action.txt', "r")
    c = []
    lines = file.readlines()
    for i, line in enumerate(lines):
        a=float(line.split(',')[0])
        b=float(line.split(',')[-1])
        c.append((a,b))
    return c

mymap = Map()

mymap.GetUserNodes()

# Construct the robot
robot = Robot(mymap)

# c=read_file()
# print('\nFrom file: ')   
# print(c)


robot.A_Star()

if robot.foundGoal:
    robot.backtrack_path()
    c=read_file()
    print('\nFrom file: ')
    print(c)

else:
    print('The goal could not be found')
    exit()
# Visualize the path
robot.visualize()