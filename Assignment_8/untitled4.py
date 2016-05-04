# -*- coding: utf-8 -*-
"""
Created on Wed May 04 21:15:20 2016

@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,20,1000)

def draw_pic(g,l,theta0,omega0):
    g = float(g)
    l = float(l)
    theta0 = float(theta0)
    omega0 = float(omega0)
    theta=[]
    omega=[]
    theta.append(theta0)
    omega.append(omega0)
    
    for i in range(999):
        omega_new=omega[i]-(g/l)*np.sin(theta[i])*t[1]
        omega.append(omega_new)
        theta_new=theta[i]+omega[i+1]*t[1]
        theta.append(theta_new)
        
    plt.figure(figsize=(10,10))
    plt.plot(t,theta,color='black',linewidth=1)
    plt.show()  
    plt.xlabel('time(s)')
    plt.ylabel('theta(radians)')
    plt.title('Driven Pendulum')
    plt.text(15,2.8, 'theta_0=2pi/3',fontsize=10)
    
draw_pic(9.8,1,2*np.pi/3,0)

