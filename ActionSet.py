import math
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots()


def action_set(point,direction,flag):
    ang = 3.14*(point[1])/180    
    wheel_rad = 33 #m
    x = point[0][0]
    y = point[0][1]
    Wheel_dist = 160 #m
    dt = 0.1
    r2=69.10199999999999
    r1=51.8265  
    if direction == 'ZF':    #[0,r1]    Z-Zero F-First S-Second
        u1 = 0
        u2 = r1
        col='blue'
            
    elif direction == 'FZ':     #[r1,0]
        u1=r1
        u2=0
        col='yellow'
    
    elif direction == 'FF':     #[r1,r1]
        u1=r1
        u2=r1
        col='green'
    
    elif direction == 'ZS':     #[0,r2]
        u1=0
        u2=r2
        col='black'
            
    elif direction == 'SZ':     #[r2,0]
        u1=r2
        u2=0
        col='orange'
            
    elif direction == 'SS':     #[r2,r2]
        u1=r2
        u2=r2
        col='red'

    elif direction == 'FS':     #[r1,r2]
        u1=r1
        u2=r2
        col='brown'

    elif direction == 'SF':     #[r2,r1]
        u1=r2
        u2=r1
        col='cyan'
    
    c = 0     #clearly we can use these components to generate cost
    n_x = x
    n_y = y
    t=0
    while t<1:
        t= t + dt
        x_pre = n_x
        y_pre = n_y
        n_x = x_pre + ((u1+u2)*math.cos(ang)*(wheel_rad/2)*dt)
        n_y = y_pre + ((u1+u2)*math.sin(ang)*(wheel_rad/2)*dt)
        ang = ang + ((u2-u1)*(wheel_rad/Wheel_dist)*dt)
        c = c + math.sqrt((n_x-x_pre)**2 + (n_y-y_pre)**2)
        if flag==1:
            # print('\nt: ' + str(t))
            # print('xpre :' + str(x_pre))
            # print('ypre: ' + str(y_pre))
            # print('n_x: ' + str(n_x))
            # print('n_y: ' + str(n_y))
            # print('ang:' + str(180*ang/3.14))
            # print('c: ' + str(c))
            plt.plot([x_pre, n_x], [y_pre, n_y], color=col)
            
    
    n_ang = np.rad2deg(ang)
    if n_ang>=360 or n_ang<0:
        n_ang = n_ang%360       #always returns a positive number < 360
            
    new_point = ((n_x, n_y), n_ang)
    print('new point: ' + str(new_point))
    if flag==0:
        return new_point, c

def check_neighbors(cur_node):
    dires = ['ZF','FZ','FF','ZS','SZ', 'SS', 'FS', 'SF']
    neighbors = []
    costs=[]
    direc = []
    for dire in dires:
        #new_point, cost = action_set(cur_node,dire,0)
        action_set(cur_node,dire,1)
        # neighbors.append(new_point)
        # costs.append(cost)
        direc.append(dire)
    return neighbors, costs, direc


plt.grid()
ax.set_aspect('equal')
plt.xlim(-5000,5000)
plt.ylim(-5000,5000)
nei, c, d = check_neighbors(((-4500,-3000),60))
plt.show()
