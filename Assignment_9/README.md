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
  At first glance a state of chaos is a state that does not repeat itself. In this assignment the pendulum is in a chaos state when the amplitude of the driving force is large enough. The pendulum is in chaos because it does not settle into any sort of repeating steadystate behavior in Figure_1(c). To be more explicit, a state of chaos is a state which can be both deterministic and unpredictable at the same time. This kind of state is very sensetive to the initial conditions and a slight difference in the beginning may have completely different results. And since we cannot know the exact initial conditions practically, such a state is unpredictable although deterministic and thus it is chaos.<br>
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_9/F0.png) <br>Figure_1(a)<br>
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_9/F0.5.png) <br>Figure_1(b)<br>
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_9/F1.2.png) <br>Figure_1(c)<br>


























