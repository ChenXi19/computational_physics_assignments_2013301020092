# encoding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def lorenz(x, y, z, s=10, r=25, b=8.0/3):
    x_dot = s*(y - x)
    y_dot = r*x - y - x*z
    z_dot = x*y - b*z
    return x_dot, y_dot, z_dot

dt = 0.01
stepCnt = 10000

# Need one more for the initial values
xs = np.empty((stepCnt + 1,))
ys = np.empty((stepCnt + 1,))
zs = np.empty((stepCnt + 1,))

x_plot = []
y_plot = []
z_plot = []

# Setting initial values
xs[0], ys[0], zs[0] = (1.0, 0.0, 0.0)

# Stepping through "time".
for i in range(stepCnt):
    # Derivatives of the X, Y, Z state
    x_dot, y_dot, z_dot = lorenz(xs[i], ys[i], zs[i])
    xs[i + 1] = xs[i] + (x_dot * dt)
    ys[i + 1] = ys[i] + (y_dot * dt)
    zs[i + 1] = zs[i] + (z_dot * dt)
    if (zs[i]-30)*(zs[i+1]-30)<0.0:
        r = np.abs(zs[i+1]/zs[i])
        x_plot.append((xs[i]*r+xs[i+1])/(1+r))
        y_plot.append((ys[i]*r+ys[i+1])/(1+r))

"""
fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot(xs, ys, zs)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor (r = 10)")

plt.savefig('3d_10.png')
plt.show()
"""

plt.title('Poincare section(z=30)')
plt.xlabel('x')
plt.ylabel('y')

plt.scatter(x_plot,y_plot,s=1)

plt.savefig('xy_z=30sec.png')
plt.show()




