import matplotlib.pyplot as plt
from sys import exit

class Map:

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set(xlim=(-5.1, 5.1), ylim=(-5.1, 5.1))
        self.ax.set_aspect('equal')
        self.MapSide = 10.2

    def DrawSquares(self,clr):
        self.BigSide = 10
        self.SmallSide = 1.5
        
        OuterSquare = plt.Rectangle((-5.1, -5.1), self.MapSide, self.MapSide, edgecolor = 'k', facecolor = "orange")
        self.ax.add_patch(OuterSquare)
        InnerSquare = plt.Rectangle((-5, -5), self.BigSide, self.BigSide, edgecolor = 'k', facecolor = "w")
        self.ax.add_patch(InnerSquare)
        TopSquare = plt.Rectangle((-2.75, 2.25), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_patch(TopSquare)
        LeftSquare = plt.Rectangle((-4.75, -0.75), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_patch(LeftSquare)
        RightSquare = plt.Rectangle((3.25, -0.75), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_patch(RightSquare)

    def DrawCircles(self,clr):
        self.Radius = 1

        self.CenterCircleC  = (0,0)
        CenterCircle = plt.Circle(self.CenterCircleC, self.Radius, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_artist(CenterCircle)

        self.TopCircleC = (2,3)
        TopCircle = plt.Circle(self.TopCircleC, self.Radius, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_artist(TopCircle)

        self.LeftCircleC = (-2,-3)
        LeftCircle = plt.Circle(self.LeftCircleC, self.Radius, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_artist(LeftCircle)

        self.RightCircleC = (2,-3)
        RightCircle = plt.Circle(self.RightCircleC, self.Radius, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_artist(RightCircle)

    def InMap(self, point, clr):
        x = point[0]
        y = point[1]

        if x<-5 or x>5 or y<-5 or y>5:
            print("point out of bounds")
            return False
        elif -5 < x < 5 and -5 < y < 5:
            if ((x >= self.CenterCircleC[0] - (self.Radius + clr)) and (x <= self.CenterCircleC[0] + (self.Radius + clr)) and
                    (y >= self.CenterCircleC[1] - (self.Radius + clr)) and (y <= self.CenterCircleC[1] + (self.Radius + clr))):
                if ((x) ** 2 + (y) ** 2) <= (self.Radius + clr) ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= self.TopCircleC[0] - (self.Radius + clr)) and (x <= self.TopCircleC[0] + (self.Radius + clr)) and
                  (y >= self.TopCircleC[1] - (self.Radius + clr)) and (y <= self.TopCircleC[1] + (self.Radius + clr))):
                if ((x - 2) ** 2 + (y - 3) ** 2) <= (self.Radius + clr) ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= self.LeftCircleC[0] - (self.Radius + clr)) and (x <= self.LeftCircleC[0] + (self.Radius + clr)) and
                  (y >= self.LeftCircleC[1] - (self.Radius + clr)) and (y <= self.LeftCircleC[1] + (self.Radius + clr))):
                if ((x + 2) ** 2 + (y + 3) ** 2) <= (self.Radius + clr) ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= self.RightCircleC[0] - (self.Radius + clr)) and (x <= self.RightCircleC[0] + (self.Radius + clr)) and
                  (y >= self.RightCircleC[1] - (self.Radius + clr)) and (y <= self.RightCircleC[1] + (self.Radius + clr))):
                if ((x - 2) ** 2 + (y + 3) ** 2) <= (self.Radius + clr) ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= (-2.75 - clr)) and (x <= (-1.25 + clr)) and (y >= (2.25 - clr)) and (y <= (3.75 + clr))):
                if ((y - 2.25 + clr >= 0) and (y - 3.75 - clr <= 0) and (x + 2.75 + clr >= 0) and (x + 1.25 - clr <= 0)):
                    print("Square obstacle")
                    return False
            elif ((x >= (-4.75 - clr)) and (x <= -3.25 + clr) and (y >= -0.75 - clr) and (y <= 0.75 + clr)):
                if ((y + 0.75 + clr >= 0) and (y - 0.75 - clr <= 0) and (x + 4.75 + clr >= 0) and (x + 3.25 - clr <= 0)):
                    print("Square obstable")
                    return False
            elif ((x >= 3.25 - clr) and (x <= 4.75 + clr) and (y >= -0.75 - clr) and (y <= 0.75 + clr)):
                if ((y + 0.75 + clr >= 0) and (y - 0.75 - clr <= 0) and (x - 3.25 + clr >= 0) and (x - 4.75 - clr <= 0)):
                    print("Square obstacle")
                    return False
            return True
            
    def GetUserNodes(self):
        # Enter the robot radius and clearance
        print("Please enter the clearance you want between the robot and the obstacles")
        self.rob_clr = float(input('Clearance: '))
        self.rob_rad = 0.177
        self.clr = self.rob_clr + self.rob_rad
        if self.clr >= 0.35:
            print("Invalid clearance and radius values, their sum must be lesser than 0.35")
            self.GetUserNodes()
        self.DrawCircles(self.clr)
        self.DrawSquares(self.clr)
        self.StartNode()
        self.GoalNode()
        self.start = self.StartPoint
        self.goal = self.GoalPoint
        robot_circle=plt.Circle((self.StartPoint[0][0],self.StartPoint[0][1]), 0.177, color='orange')
        self.ax.add_artist(robot_circle)
        robot_circle_2=plt.Circle((self.GoalPoint[0],self.GoalPoint[1]), 0.2, color='black')
        self.ax.add_artist(robot_circle_2)
        
        print('Enter 2 velocity values for the two wheels (note max speed is 120mm/s):')
        ul = float(input('ul value (mm/s): '))
        ur = float(input('ur value (mm/s): '))
        if ul>120 or ur>100 or ul<0 or ur<0:
            print('invlaid speed values.')
        else:
            self.r1 = ul
            self.r2 = ur
        
        plt.grid()
        # plt.show()

        
    def StartNode(self):
        print('Please enter a start point (x,y,theta)')
        StartX = input('start x: ')
        StartY = input('start y: ')
        StartTheta = input('start theta: ')
        self.StartPoint = [(float(StartX), float(StartY)), int(StartTheta)]

        # Check if start point is valid in map
        if self.InMap(self.StartPoint[0], self.clr):
            pass
            # plt.plot(StartX, StartY, color='green', marker='o')
        else:
            print("The start point is not valid")
            self.StartNode()

    def GoalNode(self):
        print('Please enter a goal point (x,y)')
        GoalX = input('goal x: ')
        GoalY = input('goal y: ')
        self.GoalPoint = (float(GoalX), float(GoalY))

        # Check if goal point is valid in map
        if ((self.StartPoint[0][0] - self.GoalPoint[0])**2 + (self.StartPoint[0][1] - self.GoalPoint[1])**2) < (0.5**2):
            print("Start and Goal points are too close")
            self.GetUserNodes()
        elif self.InMap(self.GoalPoint, self.clr):
            pass
        else:
            print("The goal point is not valid")
            self.GoalNode()

if __name__ == '__main__':
    mymap = Map()
    mymap.GetUserNodes()