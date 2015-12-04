import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

N = 2000
u1, u2 = 0, 2*np.pi
v1, v2 = -1, 1
GeneratedPoints = []
fMax = 0.0168888


def f(u, v):
    return np.sqrt(1/8*v**2*np.cos(u) + v*np.cos(u/2) + 3*v**2/16 + 1)/(2*16.5499)

while len(GeneratedPoints) < N:
    u0 = (u2 - u1)*np.random.rand() + u1
    v0 = (v2 - v1)*np.random.rand() + v1
    if fMax*np.random.rand() < f(u0, v0) :
        GeneratedPoints.append( (u0, v0) )

print("Generated!")
xs = []
ys = []
zs = []
for i in range(0, len(GeneratedPoints)):
    u = GeneratedPoints[i][0]
    v = GeneratedPoints[i][1]
    xs.append((1+v/2 * np.cos(u/2)) * np.cos(u))
    ys.append((1+v/2 * np.cos(u/2)) * np.sin(u))
    zs.append(v/2 * np.sin(u/2))
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs, ys, zs)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

plt.show()
