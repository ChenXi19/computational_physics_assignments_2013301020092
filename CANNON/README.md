# Assignment_6: The Trajectory of a Cannon Shell
student name: Chen Xi  student number: 2013301020092

## Abstruct 
In this assignment, we are required to solve for the solution of the trajectory of a cannon shell. To be specific, a projectile is considered as a shell shot by a cannon. And the discussion is carried out under different conditions-a. with or without drag force and b. different ways to estimate the drag force.Factors concerning this assignment are listed as:<br>
* Euler method <br>
The Euler method is what we use to solve for the solution.
* Drag force of air <br>
A comparison between the plots under different conditions-with or without drag force-was made, taking into account the speed, angle and the maximum cannon-shot.
* The influence of the air density on the drag force<br>
A correction to the drag force is made in this section using different approaches. Two approches are used seperately, which are:
  * Isothermal: The air is considered as an ideal gas with a constant temperature.
  * Adiabatic: The air is assumed as a poor conductor with very slow or no convection.


## Introduction 
* Eular method:
* Drag Force of air：<br>
The physisc of air resistance is a very complicated problem. In general, this force can be wirten as<br>
At extremly low velocities the first term dominates, and its coefficient B1 can be calculated for objects with symple shapes. This is known as Stokes' law and is considered in most elementary texts. However, at any reasonable velocity the v2 term dominates for most objects. Moreover, B2 cannot be calculated exactly for objects even as symple as baseball. We can, however, approximately estimate B2 as follows. As an object moves through the atmosphere, it must push the air in front of it out of the way. The mass of air moved in time dt in mair     ,where    is the density of air and A the frontal area of the object. This air is then given a velocity of order v, and hence its kinetic energy is       . This is also the work done by the drag force (the force on the object due to air resistance) in time dt, so         . Putting this all together, we get<br>
* Anthor factor influencing air resistance in this problem is the variation of air density. During this process, the shell travels to a very high altitude, where the air density will be lower than sea level. As is discussed above, the air resistance is proportional to the density of the air, so the drag force at high altitude will be less than that at sea level.
  * Isothermal
  * Adiabatic

