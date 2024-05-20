import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
plt.style.use('dark_background')

dt = 0.001
steps = 200000
G = 6.674
class Body:
    def __init__(self, mass, pos_i, vel_i):
        self.mass = mass
        self.pos = pos_i
        self.vel = vel_i

def accel(b1, b2, b3):
    a1 = -G*b2.mass*(b1.pos-b2.pos)/(np.sqrt((b1.pos[0]-b2.pos[0])**2+(b1.pos[1]-b2.pos[1])**2+(b1.pos[2]-b2.pos[2])**2)**3) - G*b3.mass*(b1.pos-b3.pos)/(np.sqrt((b1.pos[0]-b3.pos[0])**2+(b1.pos[1]-b3.pos[1])**2+(b1.pos[2]-b3.pos[2])**2)**3)

    a2 = -G*b3.mass*(b2.pos-b3.pos)/(np.sqrt((b2.pos[0]-b3.pos[0])**2+(b2.pos[1]-b3.pos[1])**2+(b2.pos[2]-b3.pos[2])**2)**3) - G*b1.mass*(b2.pos-b1.pos)/(np.sqrt((b2.pos[0]-b1.pos[0])**2+(b2.pos[1]-b1.pos[1])**2+(b2.pos[2]-b1.pos[2])**2)**3)

    a3 = -G*b1.mass*(b3.pos-b1.pos)/(np.sqrt((b3.pos[0]-b1.pos[0])**2+(b3.pos[1]-b1.pos[1])**2+(b3.pos[2]-b1.pos[2])**2)**3) - G*b2.mass*(b3.pos-b2.pos)/(np.sqrt((b3.pos[0]-b2.pos[0])**2+(b3.pos[1]-b2.pos[1])**2+(b3.pos[2]-b2.pos[2])**2)**3)

    b1.vel += a1 * dt
    b2.vel += a2 * dt
    b3.vel += a3 * dt
    b1.pos += b1.vel * dt
    b2.pos += b2.vel * dt
    b3.pos += b3.vel * dt

m1, m2, m3 = 10, 20, 30
p1_i = np.array([-10., 10., -11.])
p2_i = np.array([0., 0., 0.])
p3_i = np.array([10., 10., 12.])
v1_i = np.array([-3., 0., 0.])
v2_i = np.array([0., 0., 0.])
v3_i = np.array([3., 0., 0.])
b1 = Body(m1, p1_i, v1_i)
b2 = Body(m2, p2_i, v2_i)
b3 = Body(m3, p3_i, v3_i)

p1 = np.full((steps, 3), 0.0)
p2 = np.full((steps, 3), 0.0)
p3 = np.full((steps, 3), 0.0)
v1 = np.full((steps, 3), 0.0)
v2 = np.full((steps, 3), 0.0)
v3 = np.full((steps, 3), 0.0)

for i in range(steps):
    p1[i], p2[i], p3[i] = b1.pos, b2.pos, b3.pos
    v1[i], v2[i], v3[i] = b1.vel, b2.vel, b3.vel

    accel(b1, b2, b3)

fig = plt.figure(figsize=(8, 8))
ax = plt.axes(projection="3d")
plt.gca().patch.set_facecolor('black')

plt.plot([i[0] for i in p1], [j[1] for j in p1], [k[2] for k in p1] , '^', color='green', lw = 0.05, markersize = 0.01, alpha=0.5)
plt.plot([i[0] for i in p2], [j[1] for j in p2], [k[2] for k in p2] , '^', color='red', lw = 0.05, markersize = 0.01, alpha=0.5)
plt.plot([i[0] for i in p3], [j[1] for j in p3], [k[2] for k in p3] , '^', color='blue', lw = 0.05, markersize = 0.01, alpha=0.5)

plt.axis('on')

# optional: use if reference axes skeleton is desired,
# ie plt.axis is set to 'on'
ax.set_xticks([]), ax.set_yticks([]), ax.set_zticks([])

# make panes have the same color as the background
ax.xaxis.set_pane_color((0.0, 0.0, 0.0, 1.0)), ax.yaxis.set_pane_color((0.0, 0.0, 0.0, 1.0)), ax.zaxis.set_pane_color((0.0, 0.0, 0.0, 1.0))
plt.show()
plt.close()
