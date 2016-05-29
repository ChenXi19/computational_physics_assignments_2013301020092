# -*- coding: utf-8 -*-
"""
Created on Sun May 29 11:18:03 2016

@author: 抽抽
"""

import numpy as np
import matplotlib.pyplot as plt


t=np.linspace(0,150,100000)

def draw_pic(g,l,q,F,OMEGA_D,theta0,omega0,the0,ome0):
    g = float(g)
    l = float(l)
    q = float(q)
    F = float(F)
    OMEGA_D = float(OMEGA_D)
    theta0 = float(theta0)
    omega0 = float(omega0)
    the0 = float(the0)
    ome0 = float(ome0)
    dthe0=theta0-the0
    theta=[]
    omega=[]
    the=[]
    ome=[]
    dthe=[]
    theta.append(theta0)
    omega.append(omega0)
    the.append(the0)
    ome.append(ome0)
    dthe.append(dthe0)
    
    for i in range(99999):
        omega_new=omega[i]+(-(g/l)*np.sin(theta[i])-q*omega[i]+F*np.sin(OMEGA_D*t[i]))*t[1]
        omega.append(omega_new)
        theta_new=theta[i]+omega[i+1]*t[1]
        while theta_new > np.pi:
            theta_new=theta_new-2*np.pi
        while theta_new < -np.pi:
            theta_new=theta_new+2*np.pi
        theta.append(theta_new)
        
        
        ome_new=ome[i]+(-(g/l)*np.sin(the[i])-q*ome[i]+F*np.sin(OMEGA_D*t[i]))*t[1]
        ome.append(ome_new)
        the_new=the[i]+ome[i+1]*t[1]
        while the_new > np.pi:
            the_new=theta_new-2*np.pi
        while the_new < -np.pi:
            the_new=theta_new+2*np.pi
        the.append(the_new)
        
        dthe_new=theta[i]-the[i]
        dthe.append(dthe_new)
        
    plt.figure(figsize=(10,5))
    #plt.plot(t,theta,color='black',linewidth=1)
    #plt.plot(t,the,color='red',linewidth=1)
    #plt.show() 
    plt.plot(t,dthe,color='black',linewidth=1)
    plt.show()
    plt.xlabel('time(s)')
    plt.ylabel('dtheta(radians)')
    plt.title('Driven Nonlinear Pendulum(F=1.2,dtheta_0=0.1)')
    #plt.text(35,0.085, 'q=10,F=2,OMEGA_D=3.13',fontsize=10)
    
draw_pic(9.8,9.8,0.5,1.2,0.66,0.2,0,0.3,0)