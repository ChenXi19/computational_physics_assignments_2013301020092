# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 14:20:14 2016

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
    def show_trajectory(self, labe, n):
        x = []
        y = []
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)
        if n == 1:
            subplot(121)
            plot(x,y, label = labe)
            xlabel(r'$x(m)$', fontsize=16)
            ylabel(r'$y(m)$', fontsize=16)
            title('Trajectory of cannon shell (without air drag)')
            ax = gca()
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.set_xlim(0, 55000)
            ax.set_ylim(0, 20000)
        elif n == 2:
            subplot(122)
            plot(x,y, label = labe)
            xlabel(r'$x(m)$', fontsize=16)
            #text(35367, 15000, 'With Air Drag', fontsize=10)
            title('Trajectory of cannon shell (with air drag)')
            ax = gca()
            ax.spines['right'].set_color('none')
            ax.spines['top'].set_color('none')
            ax.xaxis.set_ticks_position('bottom')
            ax.yaxis.set_ticks_position('left')
            ax.set_xlim(0, 55000)
            ax.set_ylim(0, 20000)
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
speed = 700
theta = range(30,65,5)
v_x = [speed * cos(i * pi / 180) for i in theta]
v_y = [speed * sin(i * pi / 180) for i in theta]
def nodrag():
    a = []
    b = []
    for i in range(len(theta)):
        a.append(cannon(flight_state(0, 0, v_x[i], v_y[i], 0), _dt = 0.1))
        labe = str(theta[i]) + r'$^{\circ}$'
        a[i].shoot()
        a[i].show_trajectory(labe,1)
        legend(loc='upper left', frameon=False)
        b.append(drag_cannon(flight_state(0, 0, v_x[i], v_y[i], 0), _dt = 0.1))
        b[i].shoot()
        b[i].show_trajectory(labe,2)
        legend(loc='upper left', frameon=False)
nodrag()
show()