import matplotlib.pyplot as plt

class Map:

    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ax.set(xlim=(-5.1, 5.1), ylim=(-5.1, 5.1))
        self.MapSide = 10.2

    def DrawSquares(self,clr):
        self.BigSide = 10
        self.SmallSide = 1.5
        InnerSquare = plt.Rectangle((-5, -5), self.BigSide, self.BigSide, edgecolor = 'k', facecolor = "none")
        self.ax.add_patch(InnerSquare)
        TopSquare = plt.Rectangle((-2.75, 2.25), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = "none")
        self.ax.add_patch(TopSquare)
        LeftSquare = plt.Rectangle((-4.75, -0.75), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = "none")
        self.ax.add_patch(LeftSquare)
        RightSquare = plt.Rectangle((3.25, -0.75), self.SmallSide, self.SmallSide, edgecolor = 'k', facecolor = "none")
        self.ax.add_patch(RightSquare)

    def DrawCircles(self,clr):
        self.Radius = 1
        self.CenterCircleC  = (0,0)
        CenterCircle = plt.Circle(self.CenterCircleC, self.Radius, edgecolor = 'k', facecolor = "none")
        self.ax.add_artist(CenterCircle)
        self.TopCircleC = (2,3)
        TopCircle = plt.Circle(self.TopCircleC, self.Radius, edgecolor = 'k', facecolor = "none")
        self.ax.add_artist(TopCircle)
        self.LeftCircleC = (-2,-3)
        LeftCircle = plt.Circle(self.LeftCircleC, self.Radius, edgecolor = 'k', facecolor = "none")
        self.ax.add_artist(LeftCircle)
        self.RightCircleC = (2,-3)
        RightCircle = plt.Circle(self.RightCircleC, self.Radius, edgecolor = 'k', facecolor = "none")
        self.ax.add_artist(RightCircle)

    def InMap(self, point):
        x = point[0]
        y = point[1]
        if -5.1 <= x < 5.1 and -5.1 <= y < 5.1:
            if ((x >= self.CenterCircleC[0] - self.Radius) and (x <= self.CenterCircleC[0] + self.Radius) and
                    (y >= self.CenterCircleC[1] - self.Radius) and (y <= self.CenterCircleC[1] + self.Radius)):
                if ((x) ** 2 + (y) ** 2) <= self.Radius ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= self.TopCircleC[0] - self.Radius) and (x <= self.TopCircleC[0] + self.Radius) and
                  (y >= self.TopCircleC[1] - self.Radius) and (y <= self.TopCircleC[1] + self.Radius)):
                if ((x - 2) ** 2 + (y - 3) ** 2) <= self.Radius ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= self.LeftCircleC[0] - self.Radius) and (x <= self.LeftCircleC[0] + self.Radius) and
                  (y >= self.LeftCircleC[1] - self.Radius) and (y <= self.LeftCircleC[1] + self.Radius)):
                if ((x + 2) ** 2 + (y + 3) ** 2) <= self.Radius ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= self.RightCircleC[0] - self.Radius) and (x <= self.RightCircleC[0] + self.Radius) and
                  (y >= self.RightCircleC[1] - self.Radius) and (y <= self.RightCircleC[1] + self.Radius)):
                if ((x - 2) ** 2 + (y + 3) ** 2) <= self.Radius ** 2:
                    print("Circular obstacle")
                    return False
            elif ((x >= -2.75) and (x <= -1.25) and (y >= 2.25) and (y <= 3.75)):
                if ((y - 2.25 >= 0) and (y - 3.75 <= 0) and (x + 2.75 >= 0) and (x + 1.25 <= 0)):
                    print("Square obstacle")
                    return False
            elif ((x >= -4.75) and (x <= -3.25) and (y >= -0.75) and (y <= 0.75)):
                if ((y + 0.75 >= 0) and (y - 0.75 <= 0) and (x + 4.75 >= 0) and (x + 3.25 <= 0)):
                    print("Square obstable")
                    return False
            elif ((x >= 3.25) and (x <= 4.75) and (y >= -0.75) and (y <= 0.75)):
                if ((y + 0.75 >= 0) and (y - 0.75 <= 0) and (x - 3.25 >= 0) and (x - 4.75 <= 0)):
                    print("Square obstacle")
                    return False
            elif ((x >= -5.1) and (x <= -5) and (y >= -5.1) and (y <= -5) and (x >= 5) and (x <= 5.1) and (y >= 5) and (
                    y <= 5.1)):
                if ((y + 5 <= 0) and (y - 5 >= 0) and (x - 5 >= 0) and (x + 5 <= 0)):
                    print("Boundary obstacle")
                    return False
        return True

    def get_user_nodes(self):
        # Enter the robot radius and clearance
        print("Please enter the clearance you want between the robot and the obstacles and the robot radius")
        self.rob_clr = float(input('Clearance: '))
        self.rob_rad = float(input('Robot Radius: '))
        self.clr = self.rob_clr + self.rob_rad

        self.DrawCircles(self.clr)
        self.DrawSquares(self.clr)
        plt.show()

        print('Please enter a start point (x,y,theta)')
        start_str_x = input('start x: ')
        start_str_y = input('start y: ')
        start_str_theta = input('start theta:')
        start_point = [(float(start_str_x), float(start_str_y)), int(start_str_theta)]

        # Check if start point is valid in maze
        if self.InMap(start_point[0]):
            pass
        else:
            print("The start point is not valid")
            self.get_user_nodes()
            exit()

        print('Please enter a goal point (x,y)')
        goal_str_x = input('start x: ')
        goal_str_y = input('start y: ')
        goal_point = (float(goal_str_x), float(goal_str_y))

        # Check if goal point is valid in maze
        if self.InMap(goal_point):
            pass
        else:
            print("The goal point is not valid")
            self.get_user_nodes()
            exit()

        self.start = start_point
        self.goal = goal_point

if __name__ == '__main__':
    mymap = Map()
    mymap.get_user_nodes()