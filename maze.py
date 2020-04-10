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

        InnerSquare = plt.Rectangle((-5, -5), self.BigSide, self.BigSide, edgecolor = 'k', facecolor = "none")
        self.ax.add_patch(InnerSquare)

        TopSquareCl = plt.Rectangle((-2.75, 2.25), self.SmallSide + clr, self.SmallSide + clr, edgecolor = 'r', facecolor = 'r')
        self.ax.add_patch(TopSquareCl)
        TopSquareClr = plt.Rectangle((-1.25, 3.75), self.SmallSide + clr, self.SmallSide + clr, angle = 180, edgecolor = 'r', facecolor = 'r')
        self.ax.add_patch(TopSquareClr)
        TopSquareL = plt.Rectangle((-2.75, 3.75), clr, clr, angle=90, edgecolor='r', facecolor='r')
        self.ax.add_patch(TopSquareL)
        TopSquareR = plt.Rectangle((-1.25, 2.25), clr, clr, angle=270, edgecolor='r', facecolor='r')
        self.ax.add_patch(TopSquareR)
        TopSquare = plt.Rectangle((-2.75, 2.25), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = 'w')
        self.ax.add_patch(TopSquare)

        LeftSquareCl = plt.Rectangle((-4.75, -0.75), self.SmallSide + clr, self.SmallSide + clr, edgecolor = 'r', facecolor = 'r')
        self.ax.add_patch(LeftSquareCl)
        LeftSquareClr = plt.Rectangle((-3.25, 0.75), self.SmallSide + clr, self.SmallSide + clr, angle = 180, edgecolor = 'r', facecolor = 'r')
        self.ax.add_patch(LeftSquareClr)
        LeftSquareL = plt.Rectangle((-4.75, 0.75), clr, clr, angle=90, edgecolor='r', facecolor='r')
        self.ax.add_patch(LeftSquareL)
        LeftSquareR = plt.Rectangle((-3.25, -0.75), clr, clr, angle=270, edgecolor='r', facecolor='r')
        self.ax.add_patch(LeftSquareR)
        LeftSquare = plt.Rectangle((-4.75, -0.75), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = 'w')
        self.ax.add_patch(LeftSquare)

        RightSquareCl = plt.Rectangle((3.25, -0.75), self.SmallSide + clr, self.SmallSide + clr, edgecolor = 'r', facecolor = 'r')
        self.ax.add_patch(RightSquareCl)
        RightSquareClr = plt.Rectangle((4.75, 0.75), self.SmallSide + clr, self.SmallSide + clr, angle = 180, edgecolor = 'r', facecolor = 'r')
        self.ax.add_patch(RightSquareClr)
        RightSquareL = plt.Rectangle((3.25, 0.75), clr, clr, angle=90, edgecolor='r', facecolor='r')
        self.ax.add_patch(RightSquareL)
        RightSquareR = plt.Rectangle((4.75, -0.75), clr, clr, angle=270, edgecolor='r', facecolor='r')
        self.ax.add_patch(RightSquareR)
        RightSquare = plt.Rectangle((3.25, -0.75), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = 'w')
        self.ax.add_patch(RightSquare)

    def DrawCircles(self,clr):
        self.Radius = 1

        self.CenterCircleC  = (0,0)
        CenterCircleClr = plt.Circle(self.CenterCircleC, self.Radius + clr, edgecolor = 'r', facecolor = 'r')
        self.ax.add_artist(CenterCircleClr)
        CenterCircle = plt.Circle(self.CenterCircleC, self.Radius, edgecolor = 'k', facecolor = 'w')
        self.ax.add_artist(CenterCircle)

        self.TopCircleC = (2,3)
        TopCircleClr = plt.Circle(self.TopCircleC, self.Radius + clr, edgecolor = 'r', facecolor = 'r')
        self.ax.add_artist(TopCircleClr)
        TopCircle = plt.Circle(self.TopCircleC, self.Radius, edgecolor = 'k', facecolor = 'w')
        self.ax.add_artist(TopCircle)

        self.LeftCircleC = (-2,-3)
        LeftCircleClr = plt.Circle(self.LeftCircleC, self.Radius + clr, edgecolor='r', facecolor='r')
        self.ax.add_artist(LeftCircleClr)
        LeftCircle = plt.Circle(self.LeftCircleC, self.Radius, edgecolor = 'k', facecolor = 'w')
        self.ax.add_artist(LeftCircle)

        self.RightCircleC = (2,-3)
        RightCircleClr = plt.Circle(self.RightCircleC, self.Radius + clr, edgecolor='r', facecolor='r')
        self.ax.add_artist(RightCircleClr)
        RightCircle = plt.Circle(self.RightCircleC, self.Radius, edgecolor = 'k', facecolor = 'w')
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
        print("Please enter the clearance you want between the robot and the obstacles and the robot radius")
        self.RobClr = float(input('Clearance: '))
        self.RobRad = float(input('Robot Radius: '))
        self.clr = self.RobClr + self.RobRad
        if self.clr >= 0.25:
            print("Invalid clearance and radius values, their sum must be lesser than 0.25")
            self.GetUserNodes()
        self.DrawCircles(self.clr)
        self.DrawSquares(self.clr)
        plt.show()

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
        GoalX = input('start x: ')
        GoalY = input('start y: ')
        self.GoalPoint = (float(GoalX), float(GoalY))

        # Check if goal point is valid in map
        if self.StartPoint[0] == self.GoalPoint:
            print("Start and Goal points are the same")
            self.GoalNode()
        elif self.InMap(self.GoalPoint, self.clr):
            pass
        else:
            print("The goal point is not valid")
            self.GoalNode()

        self.start = self.StartPoint
        self.goal = self.GoalPoint

        self.DrawCircles(self.clr)
        self.DrawSquares(self.clr)
        plt.show()


if __name__ == '__main__':
    mymap = Map()
    mymap.GetUserNodes()
    mymap.StartNode()
    mymap.GoalNode()