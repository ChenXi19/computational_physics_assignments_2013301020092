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
  where ![](http://latex.codecogs.com/gif.latex?%5COmega%3D%5Csqrt%7Bg/l%7D),and ![](http://latex.codecogs.com/gif.latex?%5Ctheta_0%2C%5Cvarphi) depend on the initial conditions- the initial speed and displacement of the pendulum. And in this case, the angular frequency ![](http://latex.codecogs.com/gif.latex?%5COmega%3D%5Csqrt%7Bg/l%7D) is independent of m and the amplitude of the motion. However if we solve for the nonlinear equation, we will find that the angular frequency is influenced by the amplitude of the motion. [2]<br>

* Dissipation<br>
  To be a bit more realistic, we add friction to this system. In many case the damping force is proportional to the velocity and thus the friction force is of the form ![](http://latex.codecogs.com/gif.latex?-q%28d%5Ctheta/dt%29), where q is the parameter that measures the strength of the damping and the minus sign guarantees that the force will always oppose the motion of the pendulum.[2] <br>

* Driven force<br> 
  To discuss a more interesting problem, a driven force is added to the system, which is of the form ![](http://latex.codecogs.com/gif.latex?F_Dsin%28%5COmega_Dt%29). The amplitude of the force is ![](http://latex.codecogs.com/gif.latex?F_D) and the angular frequency is ![](http://latex.codecogs.com/gif.latex?\Omega_D). This leads to the equation of motion:<br>
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%5Ctheta%7D%7Bdt%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta-q%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_Dsin%28%5COmega_Dt%29)<br>

* Euler-Cromer method <br>
  The Euler method is no longer suitable for the oscillatory problem, while a slight modification will save this method which yields the Euler-Cromer method. We use simple pendulum to illustrate this method, where there is no damping, driven force or nonlinearity. And the equation of motion is:<br>
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%5Ctheta%7D%7Bdt%5E2%7D%20%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta)<br>
  The exact solution is:<br>
  ![](http://latex.codecogs.com/gif.latex?%5Ctheta%3D%5Ctheta_0sin%28%5COmega%20t&plus;%5Cvarphi%20%29)<br>

  We can also solve this equation by Euler method and the calculate subroutine is:<br>
  ![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D-%28g/l%29%5Ctheta_i%5CDelta%20t%5C%5C%20%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi%7D%5CDelta%20t%5C%5C%20t_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t%20%5Cend%7Bmatrix%7D)<br>
  
  while the subroutine for Euler-Cromer method is:<br>
  ![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D-%28g/l%29%5Ctheta_i%5CDelta%20t%5C%5C%20%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t%5C%5C%20t_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t%20%5Cend%7Bmatrix%7D)<br>

  As is clear, the only difference between the Euler method and the Euler-Cromer method is the way we calculate the new value of ![](http://latex.codecogs.com/gif.latex?\theta): Euler method uses the previous value of ![](http://latex.codecogs.com/gif.latex?\omega) and ![](http://latex.codecogs.com/gif.latex?\theta) to calculate the new value of ![](http://latex.codecogs.com/gif.latex?\theta) while the Euler-Cromer method uses the previous value of ![](http://latex.codecogs.com/gif.latex?\theta) and the new value of ![](http://latex.codecogs.com/gif.latex?\omega) to calculate the new value of ![](http://latex.codecogs.com/gif.latex?\theta). Indeed, for many problem it makes no significant difference. Yet, for problems involving oscillatory motion the Euler-Cromer method conserves energy over each complete period of the motion. The effectiveness of Euler-Cromer method comparing to the Euler method can be seen below.
  And the results using different methods is:<br>
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_8/QQ%E6%88%AA%E5%9B%BE20160504202535.png)<br>
  (![For the source code please click here.](https://github.com/ChenXi19/computational_physics_assignments_2013301020092/blob/master/Assignment_8/untitled0.py)) <br>
  
  
  
## Results 
### Damped pendulum
![Source code](https://github.com/ChenXi19/computational_physics_assignments_2013301020092/blob/master/Assignment_8/untitled2.py)[1]<br>
By Euler-Cromer method, the equation of motion is<br>
![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D&plus;%28-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta_i-q%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D%29%5CDelta%20t%5C%5C%20%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t%5C%5C%20t_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t%20%5Cend%7Bmatrix%7D)<br>
In this way the numerical results is shown below<br>
![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_8/damped.png) <br>
Figure_2 ![](http://latex.codecogs.com/gif.latex?%5Ctheta) as a function of time for a damped pendulum for several different value of the damping, q, calculated by the Euler-Cromer method. Here we have taken g=9.8 and l=1.0.<br>

Above shows how damping influence the oscillatory behavior: there are three different kinds of behavior under different damping- underdamped, overdamped and critically damped. The blue line represents the underdamped behavior, where the friction is small and the pendulum stops over a period of oscillation. The overdamped behavior is represented by the red line where the fricion is large and the pendulum also comes to the stable state slowly due to the small velocity caused by the large damping. And the green line represents the critical damped behavior because the pendulum comes to the stable state in the shortest time.<br>

### The motion of linear forced pendulum with friction
The equation of motion for the linear forced pendulum with friction is:<br>
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%5Ctheta%7D%7Bdt%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta-q%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_Dsin%28%5COmega_Dt%29)<br>
The the calculative subroutine with the Euler-Cromer method is:<br>
![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20%5Comega_%7Bi&plus;1%7D%3D%5Comega_%7Bi%7D&plus;%28-%5Cfrac%7Bg%7D%7Bl%7D%5Ctheta_i-q%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_Dsin%28%5COmega_Dt%29%29%5CDelta%20t%5C%5C%20%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t%5C%5C%20t_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t%20%5Cend%7Bmatrix%7D) <br>
Solving the equation, we get several interesting results concerning the motion of the pendulum:




## Reference
[1] The figure is from ![Wiki Pendulum](https://simple.wikipedia.org/wiki/Pendulum)
[2] Computational physiss, second edition, Nicholas J. Giordano
[3] The source code is from my classmate ![Wu Yuqiao](https://github.com/wuyuqiao/computationalphysics_N2013301020142/blob/master/chapter3/pendulum.md)<br>
















