# Assignment_7 Effect of backspin on a batted ball
Student name: Chen Xi<br>Student number: 2013301020092<br>

## Abstract
In this assignment, a discussion on the effect of backspin will be carried out.The key factor is air ressitance, which mainly depends on the spin of the batted ball. The air resistance is also influenced by the roughness and smothness of the ball but this will not be discussed in this assignment. To solve for the trajectory of the ball, Euler method is applied and also the Magnus effect will be introduced to demonstrate how the spin affact the motion of the ball.


Key words: Backspin, Air resistance, Magnus effect

## Introduction
* Drag force of air<br>
The physisc of air resistance is a very complicated problem. In general, this force can be wirten as<br>![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-B_1v-B_2v%5E2)<br>
At extremly low velocities the first term dominates, and its coefficient B1 can be calculated for objects with symple shapes. This is known as Stokes' law and is considered in most elementary texts. However, at any reasonable velocity the second term dominates for most objects. Moreover, B2 cannot be calculated exactly for objects even as symple as baseball. We can, however, approximately estimate B2 as follows. As an object moves through the atmosphere, it must push the air in front of it out of the way. The mass of air moved in time dt in ![](http://latex.codecogs.com/gif.latex?m_%7Bair%7D%5Csim%20%5Crho%20Avdt),where ![](http://latex.codecogs.com/gif.latex?%5Crho) is the density of air and A the frontal area of the object. This air is then given a velocity of order v, and hence its kinetic energy is ![](http://latex.codecogs.com/gif.latex?E_%7Bair%7D%5Csim%20m_%7Bair%7Dv%5E2/2). This is also the work done by the drag force (the force on the object due to air resistance) in time dt, so ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7Dvdt%3DE_%7Bair%7D). Putting this all together, we get<br> ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-%5Cfrac%7B1%7D%7B2%7DC%5Crho%20Av%5E2)

* The Magnus froce<br>
  The drag force has the form ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5Csim%20v%5E2), where v is the speed of the object relative to the air. For a ball spinning about the axis perpendicular to the direction of travel, this speed will be different on opposite edges of the ball, as illustrated below.<br>
  ![]()<br>
  Because of the spin, the edge of the ball at the bottom in Figure_1 will have a larger velocity relative to the air than will the edge of the ball at the top of the figure. This will result in a larger drag force edge of the ball where the velocity is highest than on the opposite edge. When the forces on the two sides of the ball are added together, there will be a net force in the -z direction. This is known as Magnus force.<br>
  To understand how the Magnus force depends on the angular velocity of the ball, we first note that the upward 
