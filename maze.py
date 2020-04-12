import matplotlib.pyplot as plt
from sys import exit

class Map:

    def __init__(self):
        
        self.fig, self.ax = plt.subplots()
        self.ax.set(xlim=(-5100, 5100), ylim=(-5100, 5100))
        self.ax.set_aspect('equal')
        self.MapSide = 10200

    def DrawSquares(self,clr):
        self.BigSide = 10000
        self.SmallSide = 1500
        
        OuterSquare = plt.Rectangle((-5100, -5100), self.MapSide, self.MapSide, edgecolor = 'k', facecolor = "orange")
        self.ax.add_patch(OuterSquare)
        InnerSquare = plt.Rectangle((-5000, -5000), self.BigSide, self.BigSide, edgecolor = 'k', facecolor = "w")
        self.ax.add_patch(InnerSquare)
        TopSquare = plt.Rectangle((-2750, 2250), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_patch(TopSquare)
        LeftSquare = plt.Rectangle((-4750, -750), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_patch(LeftSquare)
        RightSquare = plt.Rectangle((3250, -750), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_patch(RightSquare)

    def DrawCircles(self,clr):
        self.Radius = 1000

        self.CenterCircleC  = (0,0)
        CenterCircle = plt.Circle(self.CenterCircleC, self.Radius, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_artist(CenterCircle)

        self.TopCircleC = (2000,3000)
        TopCircle = plt.Circle(self.TopCircleC, self.Radius, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_artist(TopCircle)

        self.LeftCircleC = (-2000,-3000)
        LeftCircle = plt.Circle(self.LeftCircleC, self.Radius, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_artist(LeftCircle)

        self.RightCircleC = (2000,-3000)
        RightCircle = plt.Circle(self.RightCircleC, self.Radius, edgecolor = 'k', facecolor = 'orange')
        self.ax.add_artist(RightCircle)

    def InMap(self, point, clr):
        x = point[0]
        y = point[1]

        if x<-(5000-clr) or x>(5000-clr) or y<-(5000-clr) or y>(5000-clr):
            print("point out of bounds")
            return False
        elif -(5000-clr) < x < (5000-clr) and -(5000-clr) < y < (5000-clr):
            if ((x >= self.CenterCircleC[0] - (self.Radius + clr)) and (x <= self.CenterCircleC[0] + (self.Radius + clr)) and
                    (y >= self.CenterCircleC[1] - (self.Radius + clr)) and (y <= self.CenterCircleC[1] + (self.Radius + clr))):
                if ((x) ** 2 + (y) ** 2) <= (self.Radius + clr) ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= self.TopCircleC[0] - (self.Radius + clr)) and (x <= self.TopCircleC[0] + (self.Radius + clr)) and
                  (y >= self.TopCircleC[1] - (self.Radius + clr)) and (y <= self.TopCircleC[1] + (self.Radius + clr))):
                if ((x - 2000) ** 2 + (y - 3000) ** 2) <= (self.Radius + clr) ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= self.LeftCircleC[0] - (self.Radius + clr)) and (x <= self.LeftCircleC[0] + (self.Radius + clr)) and
                  (y >= self.LeftCircleC[1] - (self.Radius + clr)) and (y <= self.LeftCircleC[1] + (self.Radius + clr))):
                if ((x + 2000) ** 2 + (y + 3000) ** 2) <= (self.Radius + clr) ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= self.RightCircleC[0] - (self.Radius + clr)) and (x <= self.RightCircleC[0] + (self.Radius + clr)) and
                  (y >= self.RightCircleC[1] - (self.Radius + clr)) and (y <= self.RightCircleC[1] + (self.Radius + clr))):
                if ((x - 2000) ** 2 + (y + 3000) ** 2) <= (self.Radius + clr) ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= (-2750 - clr)) and (x <= (-1250 + clr)) and (y >= (2250 - clr)) and (y <= (3750 + clr))):
                if ((y - 2250 + clr >= 0) and (y - 3750 - clr <= 0) and (x + 2750 + clr >= 0) and (x + 1250 - clr <= 0)):
                    print("Square obstacle")
                    return False
            elif ((x >= (-4750 - clr)) and (x <= -3250 + clr) and (y >= -750 - clr) and (y <= 750 + clr)):
                if ((y + 750 + clr >= 0) and (y - 750 - clr <= 0) and (x + 4750 + clr >= 0) and (x + 3250 - clr <= 0)):
                    print("Square obstable")
                    return False
            elif ((x >= 3250 - clr) and (x <= 4750 + clr) and (y >= -750 - clr) and (y <= 750 + clr)):
                if ((y + 750 + clr >= 0) and (y - 750 - clr <= 0) and (x - 250 + clr >= 0) and (x - 4750 - clr <= 0)):
                    print("Square obstacle")
                    return False
            return True
            
    def GetUserNodes(self):
        # Enter the robot radius and clearance
        print("Please enter the clearance you want between the robot and the obstacles")
        self.rob_clr = float(input('Clearance (in mm): '))
        self.rob_rad = 105
        self.clr = self.rob_clr + self.rob_rad
        if self.clr >= 350:
            print("Invalid clearance and radius values, their sum must be lesser than 350")
            self.GetUserNodes()
        self.DrawCircles(self.clr)
        self.DrawSquares(self.clr)
        self.StartNode()
        self.GoalNode()
        self.start = self.StartPoint
        self.goal = self.GoalPoint
        robot_circle=plt.Circle((self.StartPoint[0][0],self.StartPoint[0][1]), 105, color='black')
        self.ax.add_artist(robot_circle)
        robot_circle_2=plt.Circle((self.GoalPoint[0],self.GoalPoint[1]), 200, color='blue')
        self.ax.add_artist(robot_circle_2)
        
        print('Enter 2 RPM values for the two wheels (note max RPM is 27RPM, as max rotational speed is 162.72 deg/s):')
        ul = float(input('RPM1 value : '))
        ur = float(input('RPM2 value : '))
        if ul>27 or ur>27 or ul<0 or ur<0:
            print('invlaid rpm values.')
        else:
            self.r1 = ul*0.1047*33     #converting to rad/s
            self.r2 = ur*0.1047*33     #converting to rad/s
            print('r1:' + str(self.r1))
            print('r2:' + str(self.r2))

        
    def StartNode(self):
        print('Please enter a start point (x,y,theta)')
        StartX = input('start x: ')
        StartY = input('start y: ')
        StartTheta = input('start theta: ')
        self.StartPoint = [(float(StartX), float(StartY)), int(StartTheta)]

        # Check if start point is valid in map
        if self.InMap(self.StartPoint[0], self.clr):
            pass
        else:
            print("The start point is not valid")
            self.StartNode()

    def GoalNode(self):
        print('Please enter a goal point (x,y)')
        GoalX = input('goal x: ')
        GoalY = input('goal y: ')
        self.GoalPoint = (float(GoalX), float(GoalY))

        # Check if goal point is valid in map
        if ((self.StartPoint[0][0] - self.GoalPoint[0])**2 + (self.StartPoint[0][1] - self.GoalPoint[1])**2) < (500**2):
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