# Assignment_9 A DISCUSSION ON CHAOS AND THE CONSTRUCTION of POINCARE SECTIONS
student name: CHEN XI<br>
student number: 2013301020092

## Abstract 
In this assignment we are required to construct the Poincare sections of a driven nonlinear pedulum at times where  ![](http://latex.codecogs.com/gif.latex?%5COmega_Dt%3D%5Cfrac%7B%5Cpi%20%7D%7B2%7D&plus;2%5Cpi%20n) so that the drive force reaches its maximum or at times ![](http://latex.codecogs.com/gif.latex?%5Cpi%20/4) out of phase. And the a comparison will be made to show the difference or similarities between those sections. Some important concepts, like chaos, phase space etc.,are included and the Poincare section is adopted to deal with chaos.


## Introduction
* A driven nonlinear pendulum<br>
  
  The case that we will be discussing is pendulum when dissipation, an external driving force and nonlinearity is present. Hence we have the equation of motion as following:<br>

  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2%20%5Ctheta%7D%7Bdt%5E2%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%20%5Ctheta%20&plus;q%5Cfrac%7Bd%20%5Ctheta%7D%7Bdt%7D&plus;F_Dsin%28%5COmega_Dt%29)
  
  where the friction is of the form ![](http://latex.codecogs.com/gif.latex?q%5Cfrac%7Bd%20%5Ctheta%7D%7Bdt%7D) and ![](http://latex.codecogs.com/gif.latex?F_Dsin%28%5COmega_Dt%29) is the external driving force and ![](http://latex.codecogs.com/gif.latex?-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta) indicates nonlinearity. This can also be rewrite as two first-order differential equations as below:
  
  ![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20%5Cfrac%7Bd%5Comega%7D%7Bdt%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta%20-q%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_Dsin%28%5COmega_Dt%29%5C%5C%20%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D%3D%5Comega%20%5Cend%7Bmatrix%7D)
  
* Euler Cromer method<br>
  
  The Euler Cromer method is also suitable for this problem. We also adjust the value of ![](http://latex.codecogs.com/gif.latex?%5Ctheta) after each step so as to keep it in the range of ![](http://latex.codecogs.com/gif.latex?%5B%5Cpi%2C-%5Cpi%5D) and our subroutine is as below:
  
  
  For each step i calculate ![](http://latex.codecogs.com/gif.latex?%5Comega) and ![](http://latex.codecogs.com/gif.latex?%5Ctheta)<br>
  ![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20%5Comega_%7Bi&plus;1%7D%3D%5Comega_i-%5B%28g/l%29sin%5Ctheta_i-q%5Comega_i&plus;F_Dsin%28%5COmega_Dt_i%29%5D%5CDelta%20t%5C%5C%20%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i%20&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t%20%5Cend%7Bmatrix%7D)<br>
  if ![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D) is out of the range ![](http://latex.codecogs.com/gif.latex?%5B%5Cpi%2C-%5Cpi%5D), add or substract ![](http://latex.codecogs.com/gif.latex?2%5Cpi) to keep it in this range.<br>
  ![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_i&plus;%5CDelta%20t)<br>
  Repeat.
  

* Chaos<br>
  In common usage, "chaos" means "a state of disorder". However, in chaos theory, the term is defined more precisely. Although no universally accepted mathematical definition of chaos exists, a commonly used definition originally formulated by Robert L. Devaney says that, for a dynamical system to be classified as chaotic, it must have these properties:
  1. it must be sensitive to initial conditions
  2. it must be topologically mixing
  3. it must have dense periodic orbits
  In some cases, the last two properties in the above have been shown to actually imply sensitivity to initial conditions. In these cases, while it is often the most practically significant property, "sensitivity to initial conditions" need not be stated in the definition.
  If attention is restricted to intervals, the second property implies the other two.An alternative, and in general weaker, definition of chaos uses only the first two properties in the above list.[1]
  In this assignment the pendulum is in a chaos state when the amplitude of the driving force is large enough, because it does not settle into any sort of repeating steadystate behavior as in Figure_1(c). To be more explicit, this kind of state is very sensetive to the initial conditions and a slight difference in the beginning may have completely different results. And since we cannot know the exact initial conditions practically, such a state is unpredictable although deterministic and thus it is chaos.<br>


## Results
### The Driven Pendulum
* The oscillation plots under different conditions<br>
  Taking the driving force, damping and the nonlinearity into consideration, the motion of the pendulum becomes more interesting and below are some of the plots of its movement under different conditions:<br>
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_9/F0.png) <br>Figure_1(a)<br>
  In this plot, F_D=0 and without a driving force, the motion is dapmed and come to a rest after a few oscillations. This damped oscillations have a frequency close to the natural frequency of undamped ocsillation. The plot shows some similarities with plots of the simple harmonic pendulum and its damped cousin but is not exactly the same because of the nonlinearity.<br>


  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_9/F0.5.png) <br>Figure_1(b)<br>
  In this plot, F_D=0.5 and with a small driven force, there are two regimes. The first few oscillations are affected by the decay of an initial transient as in the case of no driving force. After the transient is damped away, the pendulum settles into a steady oscillation in response to the driving force.<br>
  
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_9/F1.2.png)
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_9/F1.2nojump.png)<br>Figure_1(c)<br>
  In those two plots F_D=1.2 and the motion is no longer simple even at long times. The vertical jumps in the above plot are due to our resetting the angle to keep it with the range ![](http://latex.codecogs.com/gif.latex?%5B%5Cpi%2C-%5Cpi%5D) and thus corresponding to the pendulum swinging over the top. Below the first plot is the plot without this resseting of the angle and the oscillation of the pendulum still does not seem to settle into any sort of steady motion. The pendulum is in chaos.<br>
  
* The angular velocity of the pendulum<br>
  When the driven force is large enough, as in this case F_D=1.2, the plot of angular velocity with respect to time also shows a lot of irregularity and chaos.
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_9/omega.png) <br>Figure_2<br> 

* Sensivity to the initial conditions
  A chaos state is very sensitive to its initial condition. Such sensivity of the driven nonlinear pendulum with F_D=1.2 is shown as below.
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_9/inisep.png)<br>Figure_3<br>
  As is obvious in the picture above the two pendulums only vary slight from each other at the beginning with the red line representing ![](http://latex.codecogs.com/gif.latex?%5Ctheta_0%3D0.3) and the black line ![](http://latex.codecogs.com/gif.latex?%5Ctheta_0%3D0.2). After a short period of time the motions of the two pendulum become compeletly different from each other. And the difference between their angles is also irregular and unpredicable as is show below. <br>

  ![](https://github.com/ChenXi19/computational_physics_assignments_2013301020092/blob/master/Assignment_9/ini_dtheta.png)<br>
  Figure_4 Results for ![](http://latex.codecogs.com/gif.latex?%5CDelta%20%5Ctheta) from our two identical pendulums.<br>

* Oscillation in phase space 
  A good method to deal with this is to plot the oscillation in the phase space, that is to plot ![](http://latex.codecogs.com/gif.latex?%5Comega) as a function of ![](http://latex.codecogs.com/gif.latex?%5Ctheta).

  ![]()



























