import matplotlib.pyplot as plt
import math
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
# plt.style.use('dark_background')

dt = 0.00001
steps = 300000
G = 1
class Body:
    def __init__(self, mass, pos_i, vel_i):
        self.mass = mass
        self.pos = pos_i
        self.vel = vel_i

def accel(b1, b2, b3):
    a1 = -G*b2.mass*(b1.pos-b2.pos)/(np.sqrt((b1.pos[0]-b2.pos[0])**2+(b1.pos[1]-b2.pos[1])**2)**3) - G*b3.mass*(b1.pos-b3.pos)/(np.sqrt((b1.pos[0]-b3.pos[0])**2+(b1.pos[1]-b3.pos[1])**2)**3)

    a2 = -G*b3.mass*(b2.pos-b3.pos)/(np.sqrt((b2.pos[0]-b3.pos[0])**2+(b2.pos[1]-b3.pos[1])**2)**3) - G*b1.mass*(b2.pos-b1.pos)/(np.sqrt((b2.pos[0]-b1.pos[0])**2+(b2.pos[1]-b1.pos[1])**2)**3)

    a3 = -G*b1.mass*(b3.pos-b1.pos)/(np.sqrt((b3.pos[0]-b1.pos[0])**2+(b3.pos[1]-b1.pos[1])**2)**3) - G*b2.mass*(b3.pos-b2.pos)/(np.sqrt((b3.pos[0]-b2.pos[0])**2+(b3.pos[1]-b2.pos[1])**2)**3)

    b1.vel += a1 * dt
    b2.vel += a2 * dt
    b3.vel += a3 * dt
    b1.pos += b1.vel * dt
    b2.pos += b2.vel * dt
    b3.pos += b3.vel * dt

m1, m2, m3 = 1, 1, 1
p1_i = np.array([.97000436, -.24308753])
p2_i = np.array([-.97000436, .24308753])
p3_i = np.array([0., 0.])
v1_i = np.array([.93240737/2,.86473/2])
v2_i = np.array([.93240737/2,.86473/2])
v3_i = np.array([-.93240737,-.86473146])
b1 = Body(m1, p1_i, v1_i)
b2 = Body(m2, p2_i, v2_i)
b3 = Body(m3, p3_i, v3_i)

p1 = np.full((steps, 2), 0.0)
p2 = np.full((steps, 2), 0.0)
p3 = np.full((steps, 2), 0.0)
v1 = np.full((steps, 2), 0.0)
v2 = np.full((steps, 2), 0.0)
v3 = np.full((steps, 2), 0.0)

for i in range(steps):
    p1[i], p2[i], p3[i] = b1.pos, b2.pos, b3.pos
    v1[i], v2[i], v3[i] = b1.vel, b2.vel, b3.vel

    accel(b1, b2, b3)

fig = plt.figure(figsize=(8, 8))
ax = plt.gca()
plt.gca().patch.set_facecolor('white')

plt.plot([i[0] for i in p1], [j[1] for j in p1], '^', color='red', lw = 0.05, markersize = 0.15, alpha=0.5)
plt.plot([i[0] for i in p2], [j[1] for j in p2], '^', color='green', lw = 0.05, markersize = 0.15, alpha=0.5)
plt.plot([i[0] for i in p3], [j[1] for j in p3], '^', color='blue', lw = 0.05, markersize = 0.15, alpha=0.5)
plt.axis('on')

ax.set_xticks([]), ax.set_yticks([])

# plt.xlim(-12, 41)
# plt.ylim(1, 70)
plt.savefig("threebody_3d_1.png")
plt.show()
plt.close()
