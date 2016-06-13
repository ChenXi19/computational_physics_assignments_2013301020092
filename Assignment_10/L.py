# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 21:37:18 2016

@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt

x = []
y = []
z = []
t = []
    
a = 10
b = 28
c = 8/3
dt = 0.0001

x.append(1)
y.append(0)
z.append(0)
t.append(0)

for i in range(500000) :
    x_new = x[i]+10*(y[i]-x[i])*dt
    y_new = y[i]+(-x[i]*z[i]+b*x[i]-y[i])*dt
    z_new = z[i]+(x[i]*y[i]-c*z[i])*dt
    t_new = t[i]+dt
    x.append(x_new)
    y.append(y_new)
    z.append(z_new)
    t.append(t_new)
    
'''
plt.title('Lorenz model y versus time (b=25)')
plt.xlabel('y')
plt.ylabel('time')
plt.plot(t,y)
plt.savefig('yt_25.png')
'''
plt.title('Lorenz model z versus x (b=28)')
plt.xlabel('x')
plt.ylabel('z')
plt.plot(x,z)
plt.savefig('xz_28.png')

