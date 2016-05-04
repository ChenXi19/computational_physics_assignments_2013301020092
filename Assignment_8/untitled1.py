# -*- coding: utf-8 -*-
"""
Created on Wed May 04 20:31:03 2016

@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,20,1000)

def draw_pic(g,l,q,F,OMEGA_D,theta0,omega0):
    g = float(g)
    l = float(l)
    q = float(q)
    F = float(F)
    OMEGA_D = float(OMEGA_D)
    theta0 = float(theta0)
    omega0 = float(omega0)
    theta=[]
    omega=[]
    theta.append(theta0)
    omega.append(omega0)
    
    for i in range(999):
        omega_new=omega[i]+(-(g/l)*theta[i]-q*omega[i]+F*np.sin(OMEGA_D*t[i]))*t[1]
        omega.append(omega_new)
        theta_new=theta[i]+omega[i+1]*t[1]
        theta.append(theta_new)
        
    plt.figure(figsize=(10,10))
    plt.plot(t,theta,color='black',linewidth=1)
    plt.show()  
    plt.xlabel('time(s)')
    plt.ylabel('theta(radians)')
    plt.title('Driven Pendulum')
    plt.text(15,1.4, 'q=0.5,F=2,OMEGA_D=3.13',fontsize=10)
    
draw_pic(9.8,1,0.5,2,3.13,0.2,0)