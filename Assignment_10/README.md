# Assignment_10 THE LORENZ MODEL
student name: CHEN XI<br>
student number: 2013301020092

## Abstract 
In this assignment, a brief introduction of the Lorenz system will be given. Also as is required by Problem3.16, we will construct different phase-space plots in this assignment.

## Introduction
* The Lorenz system<br>
  The Lorenz system is a system of ordinary differential equations (the Lorenz equations, note it is not Lorentz) first studied by Edward Lorenz. It is notable for having chaotic solutions for certain parameter values and initial conditions. In particular, the Lorenz attractor is a set of chaotic solutions of the Lorenz system which, when plotted, resemble a butterfly or the figure one.

  ![](https://upload.wikimedia.org/wikipedia/commons/1/13/A_Trajectory_Through_Phase_Space_in_a_Lorenz_Attractor.gif)<br>
  
  The lorenz attractor was first studied by Ed N. Lorenz, a meterologist, around 1963. It was derived from a simplified model of convection in the earths atmosphere. It also arises naturally in models of lasers and dynamos. The system is most commonly expressed as 3 coupled non-linear differential equations.<br>
  
  ![](http://latex.codecogs.com/gif.latex?%5Cbegin%7Bmatrix%7D%20%5Cfrac%7Bdx%7D%7Bdt%7D%3Da%28y-x%29%5C%5C%5Cfrac%7Bdy%7D%7Bdt%7D%3D-xz&plus;bx-y%20%5C%5C%20%5Cfrac%7Bdz%7D%7Bdt%7D%3Dxy-cz%5Cend%7Bmatrix%7D)<br>
  
  One commonly used set of constants is a = 10, b = 28, c = 8 / 3. Another is a = 28, b = 46.92, c = 4. "a" is sometimes known as the Prandtl number and "b" the Rayleigh number.

  The series does not form limit cycles nor does it ever reach a steady state. Instead it is an example of deterministic chaos. As with other chaotic systems the Lorenz system is sensitive to the initial conditions, two initial states no matter how close will diverge, usually sooner rather than later. 
  
* Simple analysis of the Lorenz system<br>
  
  One normally assumes that the parameters a, b,c are positive. Lorenz used the values a=10, b=8/3 and c = 28 . The system exhibits chaotic behavior for these (and nearby) values.

  If b < 1  then there is only one equilibrium point, which is at the origin. This point corresponds to no convection. All orbits converge to the origin, which is a global attractor, when b < 1 .

  A pitchfork bifurcation occurs at b = 1 , and for b > 1  two additional critical points appear at

  ![](http://latex.codecogs.com/gif.latex?%28%5Cpm%20%5Bc%20%28b-1%29%5D%5E%7B1/2%7D%2C%5Cpm%20%5Bc%20%28b-1%29%5D%5E%7B1/2%7D%2Cb-1%29)<br>

  These correspond to steady convection. This pair of equilibrium points is stable only if

  ![](http://latex.codecogs.com/gif.latex?b%5Cleq%20a%20%5Cfrac%7Ba&plus;c&plus;3%7D%7Ba-c-1%7D) 

  which can hold only for positive b if a > c + 1 . At the critical value, both equilibrium points lose stability through a Hopf bifurcation.

  When b = 28  , a = 10  , and c = 8 / 3 , the Lorenz system has chaotic solutions (but not all solutions are chaotic). Almost all initial points will tend to an invariant set - the Lorenz attractor - a strange attractor and a fractal. Its Hausdorff dimension is estimated to be 2.06 ± 0.01, and the correlation dimension is estimated to be 2.05 ± 0.01.

  The Lorenz attractor is difficult to analyze, but the action of the differential equation on the attractor is described by a fairly simple geometric model. Proving that this is indeed the case is the fourteenth problem on the list of Smale's problems. This problem was the first one to be resolved, by Warwick Tucker in 2002.

  For other values of b , the system displays knotted periodic orbits. For example, with b = 99.96  it becomes a T(3,2) torus knot.

