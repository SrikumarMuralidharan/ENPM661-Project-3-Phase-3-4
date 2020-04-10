import cv2
import numpy as np
import math
import time
import matplotlib.pyplot as plt 
from bisect import bisect_right

class Robot:
    def __init__(self,maze):
        self.maze = maze
        self.threshold = 0.1
        self.ang_thresh = 15
        
        #robot parameters from datasheet
        self.tb_rad = 0.177 #m
        self.wheel_rad = 0.038 #m
        self.Wheel_dist = 0.354 #m
        self.dt = 0.2
        self.r1 = self.maze.rpm1     #rpm
        self.r2 = self.maze.rpm2     #rpm
        
    def round_off_int(self, point):
        x = (point[0][0] + 5)/self.threshold
        y = (point[0][1] + 5)/self.threshold
        ang = point[1]
        x = int(round(x/2)*2)
        y = int(round(y/2)*2)
        ang = int((round(ang/self.ang_thresh)*self.ang_thresh)//self.ang_thresh)
        if ang==24:
            ang=0
        new_point = ((x,y),ang)
        return new_point
        
    def action_set(self,point,direction):
        ang = math.radians(point[1])    
        x = point[0][0]
        y = point[0][1]
        
        if direction == 'ZF':    #[0,r1]    Z-Zero F-First S-Second
            u1 = 0
            u2 = self.r1
            
        elif direction == 'FZ':     #[r1,0]
            u1=self.r1
            u2=0
    
        elif direction == 'FF':     #[r1,r1]
            u1=self.r1
            u2=self.r1
    
        elif direction == 'ZS':     #[0,r2]
            u1=0
            u2=self.r2
            
        elif direction == 'SZ':     #[r2,0]
            u1=self.r2
            u2=0
            
        elif direction == 'SS':     #[r2,r2]
            u1=self.r2
            u2=self.r2

        elif direction == 'FS':     #[r1,r2]
            u1=self.r1
            u2=self.r2

        elif direction == 'SF':     #[r2,r1]
            u1=self.r2
            u2=self.r1
        
        v_x = (u1+u2)*math.cos(ang)*(self.wheel_rad/2)
        v_y = (u1+u2)*math.sin(ang)*(self.wheel_rad/2)
        v_ang = (u2-u1)*self.wheel_rad/self.Wheel_dist
        
        d_x = v_x*self.dt
        d_y = v_y*self.dt
        d_ang = v_ang*self.dt
        
        dx = round(d_x*10)/10
        dy = round(d_y*10)/10
        cost = math.sqrt(dx**2 + dy**2)     #clearly we can use these components to generate cost
        
        n_ang = ang+d_ang
        n_x = x+dx*math.cos(n_ang)
        n_y = y+dy*math.sin(n_ang)
        n_ang = np.rad2deg(n_ang)
        
        if n_ang>=360 or n_ang<0:
            n_ang = n_ang%360       #always returns a positive number < 360
            
        new_point = ((n_x, n_y), n_ang)
        return new_point, cost


    def check_neighbors(self,cur_node):
        dires = ['ZF','FZ','FF','ZS','SZ', 'SS', 'FS', 'SF']
        neighbors = []
        costs=[]
        for dire in dires:
            new_point, cost = self.action_set(cur_node,dire)
            if self.maze.InMap(new_point[0],self.maze.clr):
                neighbors.append(new_point)
                costs.append(cost)
        return neighbors, costs
    
    def Cost2Go_calc(self, point, goal):
        dist = float(np.sqrt((point[0]-goal[0])**2 + (point[1]-goal[1])**2))
        dist = round(dist*10)/10
        return dist
        
    def Reached_Goal_Area(self, point, goal):
        threshold_rad = 0.5
        if ((point[0]-goal[0]) ** 2 + (point[1]-goal[1])**2 <= threshold_rad**2):
            return True
        return False
        
    def A_Star(self):
              
        start_point = self.maze.start
        goal_point = self.maze.goal
        
        #We use round off function only to represent as nodes of list
        round_stpt = self.round_off_int(start_point)
        self.nodes = []
        
        #for phase 3 our threshold value is now 0.1, so our size for cost2come and cost2go will be width/threshold = 102
        self.visited_node = np.zeros((120,120,24))
        #Setting start_node as visited:
        self.visited_node[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]]=1
            
        self.cost2come = np.full((120,120,24),np.inf)
        self.cost2go = np.full((120,120,24),np.inf)
        self.parents = np.full((120,120,24),np.nan, np.int64)

        self.nodes.append(start_point) #add the start node to nodes
        
        #set start node to have parent of -1 and cost of 0, calculate cos2go for startnode
        self.cost2come[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]] = 0
        self.cost2go[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]] = self.Cost2Go_calc(start_point[0], goal_point)
        self.parents[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]] = -1
        
        
        #setting c2c and c2g values to be the same as start point values
        c2c = 0
        c2g = self.cost2go[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]]   #setting c2g to be the same as start_points c2g
        queue1 = [0]        #queue for index
        queue2 = [c2c+c2g]  #queue forcost functions
        self.foundGoal = False
        
        while queue1:
            # Set the current node as the top of the queue and remove it
            parent = queue1.pop(0)
            
            # Setting current node to be the node at parent location
            cur_node = self.nodes[parent]
            round_cur = self.round_off_int(cur_node)
            
            #Updating c2c value at this location
            c2c = self.cost2come[round_cur[0][0]][round_cur[0][1]][round_cur[1]]
            
            #formulating neighbours around this location
            neighbors, cost = self.check_neighbors(cur_node)
            
            for i, n in enumerate(neighbors):               
                c2g=self.Cost2Go_calc(n[0],goal_point)
                print('nei:')
                print(n[0])
                round_n = self.round_off_int(n)
            
                #condition to check for unvisited node
                if self.visited_node[round_n[0][0]][round_n[0][1]][round_n[1]]==0:
                    self.nodes.append(n)
                    print('neighbor')
                    print(n)
                    # print('round value:')
                    # print(round_n)
                    self.visited_node[round_n[0][0]][round_n[0][1]][round_n[1]]=1
                    self.cost2come[round_n[0][0]][round_n[0][1]][round_n[1]]= c2c+cost[i]
                    self.parents[round_n[0][0]][round_n[0][1]][round_n[1]]=parent
                    total_cost = c2c+cost[i]+c2g
                    
                    # In order to sort and insert based on cost, we use bisect.bisect_right() 
                    # to find position in queue and we get the location as output. We use this 
                    # location to insert in both queues.
                    
                    loc = bisect_right(queue2, total_cost)
                    queue1.insert(loc, len(self.nodes)-1)
                    queue2.insert(loc, total_cost)
                                    
                   
                if c2g<0.2:
                    print("entered")
                    self.foundGoal = True
                    queue1.clear()
                    queue2.clear()
                    break
        
    def backtrack_path(self):
        #Last node is the goal node
        goal = self.nodes[-1]
        round_g = self.round_off_int(goal)      #rounding off the values for matrix representation
        parent = self.parents[round_g[0][0]][round_g[0][1]][round_g[1]]     #locating parent value from parent list
        path_nodes = [parent]   #creating list for tracing path
        
        while parent>0:
            parent_node = self.nodes[path_nodes[-1]]    #last element of path_nodes list is used as access point for nodes
            round_pnode = self.round_off_int(parent_node)   #rounding off the values for matrix representation      
            parent = int(self.parents[round_pnode[0][0]][round_pnode[0][1]][round_pnode[1]])    #Finding parent node index
            path_nodes.append(parent)   #attaching parent node index value
        self.path = [goal]      #creating list for path node points
        for ind in path_nodes:
            if ind == -1:       #progressing till start node is reached
                break
            else:
                self.path.insert(0,self.nodes[ind])     #inserting parent node at the start of list.
        print('shortest path: ')
        print(self.path)
        
    def Connect_points(self, startp, nextp):
        spx = startp[0][0]
        spy = startp[0][1]
        npx = nextp[0][0]
        npy = nextp[0][1]
        
        #as shown in sample py file, we need manhattan distance between the 2 points to draw an arrow connecting them
        l1 = npx-spx
        l2 = npy-spy
        connect = plt.Arrow(spx, spy, l1, l2, width= 0.1, color='black')
        return connect

    def visualize(self,output,path_map):
        plt.ion()
        
        if output:
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            frame_size = (800, 800)
            today = time.strftime("%m-%d__%H.%M.%S")
            videoname=str(today)
            fps_out = 50
            out = cv2.VideoWriter(str(videoname)+".mp4", fourcc, fps_out, frame_size)
            print("Writing to Video, Please Wait")
        
        if path_map:
            for n in self.nodes:
                n_x = round(n[0][0]*10)/10
                n_y = round(n[0][1]*10)/10
                #creating a small circle for each explored node:
                node_circle = plt.Circle((n_x, n_y), 0.005, edgecolor='green', facecolor='green')
                self.maze.ax.add_artist(node_circle)
                # plt.draw()
                # plt.pause(0.00001)
            
        #to draw the path taken from start to goal point:
        for i in range(len(self.path)-1):
            connect = self.Connect_points(self.path[i], self.path[i+1])
            self.maze.ax.add_artist(connect)
            # plt.draw()
            # plt.pause(0.00001)
        
        plt.show()
        if output:
            out.release()