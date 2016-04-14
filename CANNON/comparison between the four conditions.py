# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:19:56 2016

@author: 抽抽
"""

from pylab import *
from math import *
g = 9.8
b2m = 4e-5
class flight_state:
    def __init__(self, _x = 0, _y = 0, _vx = 0, _vy = 0, _t = 0):
        self.x = _x
        self.y = _y
        self.vx = _vx
        self.vy = _vy
        self.t = _t
class cannon:
    def __init__(self, _fs = flight_state(0, 0, 0, 0, 0), _dt = 0.1):
        self.cannon_flight_state = []
        self.cannon_flight_state.append(_fs)
        self.dt = _dt
    def next_state(self, current_state):
        global g
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)
    def shoot(self):
        while not(self.cannon_flight_state[-1].y < 0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
    def show_trajectory(self, labe, n, colo):
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)
        if n == 1:
            subplot(121)
            plot(x,y, label = labe, color=colo)
            xlabel(r'$x(m)$', fontsize=16)
            ylabel(r'$y(m)$', fontsize=16)
            text(4049,373, '10' + r'$^{\circ}$', color='black')
            #text(12652,4676, 'initial speed: 500m/s\n', color='black')
            #text(35367, 15000, 'initial speed: 700m/s\n' + 'firing angle: 45' + r'$^{\circ}$', color='black')
            title('Trajectory of cannon shell')
            ax = gca()
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.set_xlim(0, 18000)
            ax.set_ylim(0, 5000)
        elif n == 2:
            subplot(122)
            plot(x,y, label = labe)
            xlabel(r'$x(m)$', fontsize=16)
            text(13139,3177, 'firing angle: 45' + r'$^{\circ}$', color='black')
            text(35367, 15000, 'initial speed: *700m/s*\n' + 'firing angle: 45' + r'$^{\circ}$', fontsize=16)
            title('Trajectory of cannon shell')
            ax = gca()
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.set_xlim(0, 18000)
            ax.set_ylim(0, 5000)
        #show()
class drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)
class adiabatic_drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        factor = (1 - 6.5e-3 * current_state.y / 288.15) ** 2.5
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - factor * b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - factor * b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)
class isothermal_drag_cannon(cannon):
    def next_state(self, current_state):
        global g, b2m
        factor = exp(-current_state.y / 1e4)
        v = sqrt(current_state.vx * current_state.vx + current_state.vy * current_state.vy)
        next_x = current_state.x + current_state.vx * self.dt
        next_vx = current_state.vx - factor * b2m * v * current_state.vx * self.dt
        next_y = current_state.y + current_state.vy * self.dt
        next_vy = current_state.vy - g * self.dt - factor * b2m * v * current_state.vy * self.dt
        #print next_x, next_y
        return flight_state(next_x, next_y, next_vx, next_vy, current_state.t + self.dt)
speed = 500
theta = [10]
v_x = [speed * cos(i * pi / 180) for i in theta]
v_y = [speed * sin(i * pi / 180) for i in theta]
def wahaha():
    a = []
    b = []
    c = []
    for i in range(len(theta)):
        a.append(isothermal_drag_cannon(flight_state(0, 0, v_x[i], v_y[i], 0), _dt = 0.1))
        labe1 = 'isothermal model'
        a[i].shoot()
        a[i].show_trajectory(labe1,1,'blue')
        #legend(loc='upper left', frameon=False)
        b.append(adiabatic_drag_cannon(flight_state(0, 0, v_x[i], v_y[i], 0), _dt = 0.1))
        labe2 = 'adiabatic model'
        b[i].shoot()
        b[i].show_trajectory(labe2,1,'red')
        #legend(loc='upper left', frameon=False)
        c.append(drag_cannon(flight_state(0, 0, v_x[i], v_y[i], 0), _dt = 0.1))
        labe1 = 'No air density change'
        c[i].shoot()
        c[i].show_trajectory(labe1,1,'black')
        #legend(loc='upper left', frameon=False)
wahaha()
show()