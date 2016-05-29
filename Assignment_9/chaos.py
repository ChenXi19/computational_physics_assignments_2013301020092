# -*- coding: utf-8 -*-
"""
Created on Sat May 28 21:16:57 2016

@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,60,10000)

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
    
    for i in range(9999):
        omega_new=omega[i]+(-(g/l)*np.sin(theta[i])-q*omega[i]+F*np.sin(OMEGA_D*t[i]))*t[1]
        omega.append(omega_new)
        theta_new=theta[i]+omega[i+1]*t[1]
        while theta_new > np.pi:
            theta_new=theta_new-2*np.pi
        while theta_new < -np.pi:
            theta_new=theta_new+2*np.pi
        theta.append(theta_new)
        
    plt.figure(figsize=(10,10))
    plt.plot(theta,omega,color='black',linewidth=1)
    plt.show()  
    plt.xlabel('time(s)')
    plt.ylabel('omega(radians/s)')
    plt.title('Driven Nonlinear Pendulum(F=0.5)')
    #plt.text(35,0.085, 'q=10,F=2,OMEGA_D=3.13',fontsize=10)
    
draw_pic(9.8,9.8,0.5,0.5,0.66,0.2,0)