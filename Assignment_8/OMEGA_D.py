# -*- coding: utf-8 -*-
"""
Created on Thu May 05 23:40:36 2016

@author: 抽抽
"""

from __future__ import division
from numpy import *
from pylab import *

theta1 = [pi/20]
theta2 = [pi/20]
theta3 = [pi/20]
length = 1.0
g = 9.8
deltat = 0.01
omega1 = [0]
omega2 = [0]
omega3 = [0]
t1 = [0]
t2 = [0]
t3 = [0]
q1 = 0.5
q2 = 0.5
q3 = 0.5
F_D=1
OMEGA1=1
OMEGA2=3.13
OMEGA3=10

while t1[-1] <= 20:
    omega1.append(omega1[-1] - (g/length)*theta1[-1]*deltat - q1*omega1[-1]*deltat+F_D*sin(OMEGA1*t1[-1])*deltat)
    theta1.append(theta1[-1] + omega1[-1]*deltat)
    t1.append(t1[-1] + deltat)

while t2[-1] <= 20:
    omega2.append(omega2[-1] - (g/length)*theta2[-1]*deltat - q2*omega2[-1]*deltat+F_D*sin(OMEGA2*t2[-1])*deltat)
    theta2.append(theta2[-1] + omega2[-1]*deltat)
    t2.append(t2[-1] + deltat)

while t3[-1] <= 20:
    omega3.append(omega3[-1] - (g/length)*theta3[-1]*deltat - q3*omega3[-1]*deltat+F_D*sin(OMEGA3*t3[-1])*deltat)
    theta3.append(theta3[-1] + omega3[-1]*deltat)
    t3.append(t3[-1] + deltat)

theta1_array = array(theta1)
theta2_array = array(theta2)
theta3_array = array(theta3)

t1_array = array(t1)
t2_array = array(t2)
t3_array = array(t3)

plot(t1_array,theta1_array,label='OMEGA=1')
plot(t2_array,theta2_array,label='OMEGA=3.13')
plot(t3_array,theta3_array,label='OMEGA=10')

legend(loc='upper right',frameon=True)

title('linear forced pendulum')
xlabel('time (s)')
ylabel('angle (radians)')

xlim(0,20)
ylim(-1,1)

grid(True)