# -*- coding: utf-8 -*-
"""
Created on Thu May 05 18:50:02 2016

@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,50,10000)

def draw_pic(g,l,q,theta0,omega0):
    g = float(g)
    l = float(l)
    q = float(q)
    theta0 = float(theta0)
    omega0 = float(omega0)
    theta=[]
    omega=[]
    theta.append(theta0)
    omega.append(omega0)
    
    for i in range(9999):
        omega_new=omega[i]+(-(g/l)*theta[i]-q*omega[i])*t[1]
        omega.append(omega_new)
        theta_new=theta[i]+omega[i+1]*t[1]
        theta.append(theta_new)
        
    plt.figure(figsize=(10,10))
    plt.plot(t,theta,color='black',linewidth=1)
    plt.show()  
    plt.xlabel('time(s)')
    plt.ylabel('theta(radians)')
    plt.title('Damped Pendulum(theta_0=pi/40)')
    plt.text(35,0.085, 'q=1',fontsize=10)
    
draw_pic(9.8,1,1,np.pi/40,0)