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

## Results

* Variations of the Lorenz variable z as a function of time with different b <br>
  For small values of ρ, the system is stable and evolves to one of two fixed point attractors. When ρ is larger than 24.74, the fixed points become repulsors and the trajectory is repelled by them in a very complex way. <br>
  When b = 5, there is an initial transient, and after it decays away z is a constent, independent of time t.<br>

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/zt_5.png)<br>
  Figure_2 Variations of the Lorenz variable z as a function of time with b = 5. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.

  The same behavior is seen when b = 10, although it takes a little bit longer to wear away.

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/zt_10.png)<br>
  Figure_3 Variations of the Lorenz variable z as a function of time with b = 10. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.

  These two cases correspond to steady convective motion in the originel fluid; in this process the warm fluid produced at the bottom surface of the container rises and the cooler fluid returens from the top. 

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/zt_25.png)<br>
  Figure_4 Variations of the Lorenz variable z as a function of time with b = 25. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.
  
  
* Variations of the Lorenz variables x, y, z as a function of time at b = 25

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xt_25.png)<br>
  Figure_5 Variations of the Lorenz variable x as a function of time with b = 25. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/yt_25.png)<br>
  Figure_6 Variations of the Lorenz variable y as a function of time with b = 25. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xt_25.png)<br>
  Figure_7 Variations of the Lorenz variable z as a function of time with b = 25. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.
  
* Trajectories of the Lorenz model projected onto the x-z plane, with different b.
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xz_5.png)<br>
  Figure_7 Trajectory of the Lorenz model projected onto the x-z plane with b = 5. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xz_10.png)<br>
  Figure_8 Trajectory of the Lorenz model projected onto the x-z plane with b = 10. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xz_25.png)<br>
  Figure_9 Trajectory of the Lorenz model projected onto the x-z plane with b = 25. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.
  
* Trajectories of the Lorenz model projected onto the x-z, y-z, x-y planes at b = 25

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xy_25.png)<br>
  Figure_10 Trajectory of the Lorenz model projected onto the x-y plane with b = 25. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/zy_25.png)<br>
  Figure_11 Trajectory of the Lorenz model projected onto the y-z plane with b = 25. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xz_25.png)<br>
  Figure_12 Trajectory of the Lorenz model projected onto the x-z plane with b = 25. The calculation was performd using the Euler method with a time step of 0.0001. The initial conditions were x = 1, y = 0, z = 0.
  
  
* 3D Phase space plots for Lorenz model with different b

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/3d_5.png)<br>
  Figure_13 3D Phase space plots for Lorenz model with b = 5. The calculation was performd using the Euler method with a time step of 0.01. The initial conditions were x = 1, y = 0, z = 0.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/3d_10.png)<br>
  Figure_14 3D Phase space plots for Lorenz model with b = 10. The calculation was performd using the Euler method with a time step of 0.01. The initial conditions were x = 1, y = 0, z = 0.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/3d.png)<br>
  Figure_15 3D Phase space plots for Lorenz model with b = 25. The calculation was performd using the Euler method with a time step of 0.01. The initial conditions were x = 1, y = 0, z = 0.
  
* Phase space plots for the Lorenz model in different planes

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/yz_sec.png)<br>
  Figure_16 Phase-space plot for the Lorenz model with r = 25. Phase space plot: z versus y when x=0. The calculation was performd using the Euler method with a time step of 0.01. The initial conditions were x = 1, y = 0, z = 0.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xz_sec.png)<br>
  Figure_17 Phase-space plot for the Lorenz model with r = 25. Phase space plot: z versus x when y=0. The calculation was performd using the Euler method with a time step of 0.01. The initial conditions were x = 1, y = 0, z = 0.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xy_z=20sec.png)<br>
  Figure_14 Phase-space plot for the Lorenz model with r = 25. Phase space plot: y versus x when z=20. The calculation was performd using the Euler method with a time step of 0.01. The initial conditions were x = 1, y = 0, z = 0.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xy_z=25sec.png)<br>
  Figure_15 Phase-space plot for the Lorenz model with r = 25. Phase space plot: y versus x when z=25. The calculation was performd using the Euler method with a time step of 0.01. The initial conditions were x = 1, y = 0, z = 0.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_10/xy_sec.png)<br>
  Figure_16 Phase-space plot for the Lorenz model with r = 25. Phase space plot: y versus x when z=30. The calculation was performd using the Euler method with a time step of 0.01. The initial conditions were x = 1, y = 0, z = 0.

