import cv2
import numpy as np
import math
import time
import matplotlib.pyplot as plt 
from bisect import bisect_right

class Robot:
    def __init__(self,maze):
        self.maze = maze
        self.ang_thresh = 15
        
        #Burger robot parameters from http://emanual.robotis.com/docs/en/platform/turtlebot3/specifications/
        self.pos_thresh = 0.1
        self.tb_rad = 105 #m
        self.wheel_rad = 33 #m
        self.Wheel_dist = 160 #m
        self.dt = 0.1
        self.r1 = self.maze.r1    
        self.r2 = self.maze.r2
        
    def round_off_int(self, point):
        x = (point[0][0] + 5000)*self.pos_thresh
        y = (point[0][1] + 5000)*self.pos_thresh
        ang = point[1]
        x = int(round(x/2)*2)
        y = int(round(y/2)*2)
        ang = int((round(ang/self.ang_thresh)*self.ang_thresh)//self.ang_thresh)
        if ang==24:
            ang=0
        new_point = ((x,y),ang)
        return new_point
        
    def action_set(self,point,direction,flag):
        ang = 3.14*(point[1])/180    
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
        
        c = 0     #clearly we can use these components to generate cost
        n_x = x
        n_y = y
        t=0
        while t<1:
            t= t + self.dt
            x_pre = n_x
            y_pre = n_y
            n_x = x_pre + ((u1+u2)*math.cos(ang)*(self.wheel_rad/2)*self.dt)
            n_y = y_pre + ((u1+u2)*math.sin(ang)*(self.wheel_rad/2)*self.dt)
            
            if not self.maze.InMap((n_x,n_y), self.maze.clr):
                return point, -1
            
            ang = ang + ((u2-u1)*(self.wheel_rad/self.Wheel_dist)*self.dt)
            c = c + math.sqrt((n_x-x_pre)**2 + (n_y-y_pre)**2)
            if flag==1:
                plt.plot([x_pre, n_x], [y_pre, n_y], color='blue')
        
        n_ang = np.rad2deg(ang)
        if n_ang>=360 or n_ang<0:
            n_ang = n_ang%360
        new_point = ((n_x, n_y), n_ang)
        
        if flag==0:
            new_point = ((n_x, n_y), n_ang)
            return new_point, c    

    def check_neighbors(self,cur_node):
        dires = ['ZF','FZ','FF','ZS','SZ', 'SS', 'FS', 'SF']
        neighbors = []
        costs=[]
        direc = []
        for dire in dires:
            new_point, cost = self.action_set(cur_node,dire,0)
            if self.maze.InMap(new_point[0],self.maze.clr) and cost!=-1:
                neighbors.append(new_point)
                costs.append(cost)
                direc.append(dire)
        return neighbors, costs, direc
    
    def Cost2Go_calc(self, point, goal):
        dist = float(np.sqrt((point[0]-goal[0])**2 + (point[1]-goal[1])**2))
        dist = round(dist*10)/10
        return dist
        
    def A_Star(self):
              
        start_point = self.maze.start
        goal_point = self.maze.goal
        
        #We use round off function only to represent as nodes of list
        round_stpt = self.round_off_int(start_point)
        self.nodes = []
        self.direc = ['N']
        
        #for phase 3 our threshold value is now 0.1, so our size for cost2come and cost2go will be width/threshold = 102
        self.visited_node = np.zeros((1020,1020,24))
        #Setting start_node as visited:
        self.visited_node[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]]=1
            
        self.cost2come = np.full((1020,1020,24),np.inf)
        self.cost2go = np.full((1020,1020,24),np.inf)
        self.parents = np.full((1020,1020,24),np.nan, np.int64)

        self.nodes.append(start_point) #add the start node to nodes
        
        #set start node to have parent of -1 and cost of 0, calculate cos2go for startnode
        self.cost2come[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]] = 0
        self.cost2go[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]] = self.Cost2Go_calc(start_point[0], goal_point)
        self.parents[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]] = -1
        
        
        #setting c2c and c2g values to be the same as start point values
        c2c = 0
        c2g = self.cost2go[round_stpt[0][0]][round_stpt[0][1]][round_stpt[1]]   #setting c2g to be the same as start_points c2g
        queue1 = [0]        #queue for index
        queue2 = [c2c+c2g]  #queue for cost functions
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
            neighbors, cost, direc = self.check_neighbors(cur_node)
            
            for i, n in enumerate(neighbors):               
                c2g=self.Cost2Go_calc(n[0],goal_point)
                round_n = self.round_off_int(n)
            
                #condition to check for unvisited node
                if self.visited_node[round_n[0][0]][round_n[0][1]][round_n[1]]==0:
                    self.nodes.append(n)
                    self.direc.append(direc[i])
                    print('node: ' + str(n))
                    print('direc:' + str(direc[i]))
                    self.visited_node[round_n[0][0]][round_n[0][1]][round_n[1]]=1
                    self.cost2come[round_n[0][0]][round_n[0][1]][round_n[1]]= c2c+cost[i]
                    self.parents[round_n[0][0]][round_n[0][1]][round_n[1]]=parent
                    total_cost = c2c+cost[i]+c2g
                    print('cost:' + str(total_cost))
                    print('c2g:' + str(c2g))
                    
                    # In order to sort and insert based on cost, we use bisect.bisect_right() 
                    # to find position in queue and we get the location as output. We use this 
                    # location to insert in both queues.
                    
                    loc = bisect_right(queue2, total_cost)
                    queue1.insert(loc, len(self.nodes)-1)
                    queue2.insert(loc, total_cost)
                                    
                   
                if c2g<200:
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
        self.path_dir = [self.direc[-1]]
        for ind in path_nodes:
            if ind == -1:       #progressing till start node is reached
                break
            else:
                self.path.insert(0,self.nodes[ind])     #inserting parent node at the start of list.
                self.path_dir.insert(0,self.direc[ind])
        print('shortest path: ')
        print(self.path)
        print('shortest path dir:')
        print(self.path_dir)
        
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
            
        #to draw the path taken from start to goal point:
        for i in range(len(self.path)-1):
            connect = self.Connect_points(self.path[i], self.path[i+1])
            self.maze.ax.add_artist(connect)
            plt.draw()
            plt.pause(0.00001)
        
        plt.show()
        if output:
            out.release()