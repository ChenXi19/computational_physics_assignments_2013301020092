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

  Because of the spin ( the spin vector is perpendicular to the plane of gravity and the velocity vector), the edge of the ball at the bottom in Figure_1 will have a larger velocity relative to the air than will the edge of the ball at the top of the figure. This will result in a larger drag force edge of the ball where the velocity is highest than on the opposite edge. When the forces on the two sides of the ball are added together, there will be a net force in the y direction. This is known as Magnus force.<br>
  To understand how the Magnus force depends on the angular velocity of the ball, we first note that the upward component of the drag force on the lower half of the ball will be propotional to the square of the velocity of the surface of the ball relative to the air, i.e., ![](http://latex.codecogs.com/gif.latex?F%5Csim%20%28v&plus;r%5Comega%20%29%5E2). Similarly the downward component will be proportional to the square of the relative velocity ![](http://latex.codecogs.com/gif.latex?%28v-r%5Comega%20%29%5E2). The Magnus force is equal to the difference between these two terms<br>
  
  ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5Csim%28v&plus;r%5Comega%20%29%5E2-%28v-r%5Comega%20%29%5E2%5Csim%20vr%5Comega)<br>
  
  Thus the net spin-dependent force have the general form<br>
  
  ![](http://latex.codecogs.com/gif.latex?F_M%3DS_0%20v%5Comega)<br>
  
  For simplicity we assume the coefficient ![](http://latex.codecogs.com/gif.latex?S_0) is a constant.
  
* The equations of motion<br> 
  To calculate the trajetory of the ball, we need to consider motion in two dimensions. We let x be the axis running from the home plate to the picher and y be the height above the ground, as in Figure_1. The equation of motion for the ball are then<br>
  ![](http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20x%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_x%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7Dv_%20x%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-%5Cfrac%7BB_2%7D%7Bm%7Dvv_x%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7D%20y%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_y%5C%5C%20%5Cfrac%7B%5Cmathrm%7Bd%7Dv_%20x%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-g&plus;%5Cfrac%7BS_0v_x%5Comega%20%7D%7Bm%7D%20%5Cend%7Bmatrix%7D%5Cright.)<br>
  Here we assume the rotation axis is perpendicular to the plane of axis x and axis y, so that the Magnus force is along the y axis. Also we assume the aguler velocity ![](http://latex.codecogs.com/gif.latex?%5Comega) is a constant; that is the ball's rotation rate does not change signicantly during the course of the pitch.
