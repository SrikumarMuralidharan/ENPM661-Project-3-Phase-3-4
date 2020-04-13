******************
Project 3 Phase 4: A_Star algorithm implementation and simulation using ROS Gazebo
Group 25
Srikumar Muralidharan
Sahana Anbazhagan
******************
Libraries used:
1. rospy
2. geometry_msgs
3. matplotlib
4. sys
5. bisect
6. numpy
7. math

Dependencies:
1. Ubuntu 16.04
2. ROS Kinetic
3. turtlebot3_gazebo
4. catkin - workspace and related packages

******************
Initial Setup:

1. Create a catkin workspace and inside the src folder, clone the turtlebot3 related files from the following git links.
a. https://github.com/ROBOTIS-GIT/turtlebot3.git
b. https://github.com/ROBOTIS-GIT/turtlebot3_msgs.git
c. https://github.com/ROBOTIS-GIT/turtlebot3_simulations.git

2. If turtlebot3-gazebo package is not installed in your system, please use the following line in command prompt:
	$ sudo apt install ros-kinetic-turtlebot3-gazebo

3. Switch default version of turtlebot3's model to Burger, which we are using. The following command is to be used in your .bashrc file.
	"export TURTLEBOT3_MODEL=burger"

4. Use catkin_make to initialise your folder with all the catkin packages. Now create a new catkin package astar_imp inside src folder of your workspace and copy the files attached alongside this readme file into the newly created folder.

******************
Procedure to Run the programs:

We are considering the start point to be the same for both the cases and have accordingly written our launch files. (note clearance is in m and coordinates are in Gazebo world coordinates)

Clearance = 0.1
Start position: 
Start X = 4.5
Start Y = 3
Start Theta = 0

*******
Case 1:
******* 
Goal X = 0
Goal Y = 3
RPM1 = 15
RMP2 = 20

*******
Case 2:
******* 
Goal X = -4
Goal Y = -2
RPM1 = 15
RMP2 = 20

As mentioned in the code, maximum RPM value is 27RPM with regards to burger bot specification. So we accordingly choose our RPM values. Now, we do the following steps.

1. Open src folder of astar_imp. Run A_star_rigid.py and enter the coordinates as shown above for each of the cases.
2. A text file "action.txt" is created in our src folder, as we record the output action sets in a new text file (output of A_star_rigid.py)
3. A new graph is generated, which formulates a path from start to goal node and is given as a visual output too.
4. ***(very important) Once the output text file is generated, open ros_run.py in an editor and change the path location of action.txt according to your system.***
5. Launch ros-gazebo using the following command line in terminal.
	$ roslaunch astar_imp my_world.launch
This opens gazebo environment with our bot at the start location. In the roslaunch terminal, enter the clearance and collision values as per the case.

6. For a different start point(say 4.5,4.5), we can use the following line in terminal to launch gazebo:
	$roslaunch astar_imp my_world.launch x_pos:=4.5 y_pos:4.5 yaw:=3.14
Be sure to have the text file generated as per your launch coordinates, correctly.


