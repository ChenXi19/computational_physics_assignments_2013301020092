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
  
  The Euler Cromer method is also suitable for this problem and our subroutine is as below:
  




























