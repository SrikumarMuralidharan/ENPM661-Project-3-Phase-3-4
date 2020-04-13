******************
Project 3 Phase 3: A_Star algorithm implementation for non-holonomic constraints
Group 25
Srikumar Muralidharan
Sahana Anbazhagan
******************
Libraries used:

1. matplotlib
2. sys
3. bisect
4. numpy
5. math

Dependencies:

1. Python 3

******************
Initial Setup:

1. Place all the .py files in the same folder as the action.txt file.
2. Run the A_star_rigid.py file to see the execution.

******************
Procedure to Run the programs:

The map is in mm scale and the (0,0) is at the center of the figure, i.e., the center of the middle circle is at (0,0).
The console will prompt for the input values. An example of how the console will look like is shown below:
*******
Case 1:
*******
Clearance (in mm): 20
Please enter a start point (x,y,theta)
start x: 4500
start y: 4500
start theta:240
Please enter a goal point (x,y)
goal x: -4500
goal y: -4500
Enter 2 RPM values for the two wheels (note max RPM is 27RPM, as max rotational speed is 162.72 deg/s):
RPM1 value : 15
RPM2 value : 20

As mentioned in the code, maximum RPM value is 27RPM with regards to burger bot specification. So we accordingly choose our RPM values. 
Now, we do the following steps.

1. Run A_star_rigid.py and enter the coordinates as shown above for each of the cases.
2. A new graph is generated, which formulates a path from start to goal node and is given as a visual output too.

