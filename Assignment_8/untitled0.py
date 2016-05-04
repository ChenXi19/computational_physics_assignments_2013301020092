# -*- coding: utf-8 -*-
"""
Created on Wed May 04 17:31:10 2016

@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,8,100)

def draw_pic(g,l,theta0,omega0):
    g = float(g)
    l = float(l)
    theta0 = float(theta0)
    omega0 = float(omega0)
    theta=[]
    omega=[]
    THETA=[]
    OMEGA=[]
    theta.append(theta0)
    omega.append(omega0)
    THETA.append(theta0)
    OMEGA.append(omega0)
    
    for i in range(99):
        omega_new=omega[i]-(g/l)*theta[i]*t[1]
        theta_new=theta[i]+omega[i]*t[1]
        theta.append(theta_new)
        omega.append(omega_new)
        
    for j in range(99):
        OMEGA_new=OMEGA[j]-(g/l)*THETA[j]*t[1]
        OMEGA.append(OMEGA_new)
        THETA_new=THETA[j]+OMEGA[j+1]*t[1]
        THETA.append(THETA_new)
        
    THETA_real=theta0*np.sin((g/l)**0.5*t+np.pi/2)
    
    plt.figure(figsize=(10,10))
    plt.plot(t,theta,label='Euler method',color='green',linewidth=1,linestyle='--')
    plt.plot(t,THETA,label='Euler Cromer method',color='red',linewidth=2,linestyle='--')
    plt.plot(t,THETA_real,label='Exact solution',color='black',linewidth=1)
    plt.legend()
    plt.show()  
    plt.xlabel('time(s)')
    plt.ylabel('theta(radians)')
    plt.title('Euler method vs Euler Cromer method')
   # plt.text()
    
draw_pic(10,1,np.pi/30,0)

        
        