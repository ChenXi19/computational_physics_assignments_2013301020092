# Assignment_8 A BASIC DISCUSSION ON PENDULUM
student name: CHEN XI<br>
student number: 2013301020092

## Abstract 
In this assignment we discuss two problems: One is the motion of the linear forced pendulum with friction and the other is the nonlinear pendulum and the relationship between the amplitude and the period. The modle concerned is a simple pendulum which is a particle of mass m connected to a massless string to a rigid support. The method used to solve for the equations of motion is Euler-Cromer method. In this assignment the effectiveness of Euler_Cromer method comparing to Euler method is also discussed.


## Introduction
* Simple pendulum<br>
  A simple pendulum is a particle of mass m connected by a massless string to a rigid support. As in figure_1, there are only two forces acting on the partcle, gravity and the tension of the string. It is convinient to consider the components of these forces parallel and perpendicular to the string. The parrallel forces add to zero while the forces perpendicular to the string is given by ![](http://latex.codecogs.com/gif.latex?F_%5Ctheta%20%3D-mgsin%5Ctheta). <br>
![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_8/Simple-Pendulum-Labeled-Diagram.png)<br>
Figure_1 Simple Pendulum<br>


By Newton's second law, the equation of motion should be:<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%5Ctheta%7D%7Bdt%5E2%7D%20%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta)<br>
where l is the length of the string and g is the gravity. If we assume that ![](http://latex.codecogs.com/gif.latex?%5Ctheta) is always small so that ![](http://latex.codecogs.com/gif.latex?sin%5Ctheta%5Capprox%20%5Ctheta), then we obtain the linear equation<br>: 
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%5Ctheta%7D%7Bdt%5E2%7D%20%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta)<br>
which gives the general solution<br>
![](http://latex.codecogs.com/gif.latex?%5Ctheta%3D%5Ctheta_0sin%28%5COmega%20t&plus;%5Cvarphi%20%29)<br>
where ![](http://latex.codecogs.com/gif.latex?%5COmega%3D%5Csqrt%7Bg/l%7D),and ![](http://latex.codecogs.com/gif.latex?%5Ctheta_0%2C%5Cvarphi) depend on the initial conditions- the initial speed and displacement of the pendulum. The angular frequency ![](http://latex.codecogs.com/gif.latex?%5Ctheta_0%2C%5Cvarphi)
