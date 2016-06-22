# Assignmet_13 Electrical Potentials And Fields-Symmetry Solution of The Capacitor

Student name: Chen Xi

Student number: 2013301020092

## Abstract

In this assignment, Problem 5.7 will be discussed by using the relaxition method and also by applying symmetry. The electric potential and field of a capacitor shown in Figure_1 will be conducted. In this assignment, I only understand how the code works and what is rationale of it but have no time to write a detailed report since I still have a GRE test and several finals to prepare.

![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_13/3.png)

## Introduction:

* Laplace's Equation:
  
  In order to find the distribution of the electric field of the capacitor, we need to solve for the Laplace's equation. In mathematics, Laplace's equation is a second-order partial differential equation named after Pierre-Simon Laplace who first studied its properties. This is often written as:
  
  ![](http://latex.codecogs.com/gif.latex?%5CDelta%20%5E2%20%5Cvarphi%3D0)

  Laplace's equation and Poisson's equation are the simplest examples of elliptic partial differential equations. The general theory of solutions to Laplace's equation is known as potential theory. The solutions of Laplace's equation are the harmonic functions, which are important in many fields of science, notably the fields of electromagnetism, astronomy, and fluid dynamics, because they can be used to accurately describe the behavior of electric, gravitational, and fluid potentials. In the study of heat conduction, the Laplace equation is the steady-state heat equation.
  
  
* The relaxiation method:
 
  The method that we use to find the field is relaxiation method. In numerical mathematics, relaxation methods are iterative methods for solving systems of equations, including nonlinear systems.

  Relaxation methods were developed for solving large sparse linear systems, which arose as finite-difference discretizations of differential equations. They are also used for the solution of linear equations for linear least-squares problems and also for systems of linear inequalities, such as those arising in linear programming. They have also been developed for solving nonlinear systems of equations.

  Relaxation methods are important especially in the solution of linear systems used to model elliptic partial differential equations, such as Laplace's equation and its generalization, Poisson's equation. These equations describe boundary-value problems, in which the solution-function's values are specified on boundary of a domain; the problem is to compute a solution also on its interior. Relaxation methods are used to solve the linear equations resulting from a discretization of the differential equation, for example by finite differences.

  These iterative methods of relaxation should not be confused with "relaxations" in mathematical optimization, which approximate a difficult problem by a simpler problem, whose "relaxed" solution provides information about the solution of the original problem.

## Results:

* The potential distribution:
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_13/1.png)

* The 3D image of the potential distribution:
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_13/3D.png)

* The electric field:
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_13/2.png)

![Source Code](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_13/131.py)


## Reference:

[1] ![Laplace's equation from Wikipedia](https://en.wikipedia.org/wiki/Laplace%27s_equation)

[2] ![Relaxiation method from Wikipedia](https://en.wikipedia.org/wiki/Relaxation_(iterative_method))

[3] ![Source code from Wu Yuqiao](https://github.com/wuyuqiao/computationalphysics_N2013301020142)
