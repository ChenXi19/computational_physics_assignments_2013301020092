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
* Eular method:<br>
In mathematics and computational science, the Euler method is a first-order numerical procedure for solving ordinary differential equations (ODEs) with a given initial value. It is the most basic explicit method for numerical integration of ordinary differential equations and is the simplest Runge–Kutta method. The Euler method is named after Leonhard Euler, who treated it in his book Institutionum calculi integralis (published 1768–70).<br>The formulation of the Euler method can be listed below as:<br>Suppose we want to approximate the solution of the initial value problem.<br>![](http://latex.codecogs.com/gif.latex?y%27%28t%29%3Df%28t%2Cy%28t%29%29%2C%20y%28t_%7B0%7D%29%3Dy_%7B0%7D)<br>Choose a value h for the size of every step and set ![](http://latex.codecogs.com/gif.latex?t_%7Bn%7D%3Dt_%7B0%7D&plus;nh). Now, one step of the Euler method from ![](http://latex.codecogs.com/gif.latex?t_%7Bn%7D) to ![](http://latex.codecogs.com/gif.latex?t_%7Bn&plus;1%7D%3Dt_%7Bn%7D&plus;h) is<br> ![](http://latex.codecogs.com/gif.latex?y_%7Bn&plus;1%7D%3Dy_%7Bn%7D&plus;hf%28t_%7Bn%7D%2Cy_%7Bn%7D%5D%29) <br> The value of ![](http://latex.codecogs.com/gif.latex?y_%7Bn%7D) is an approxiamtion of the solution to the ODE at time ![](http://latex.codecogs.com/gif.latex?t_%7Bn%7D%3Ay_%7Bn%7D%5Capprox%20y%28t_%7Bn%7D%29). The Euler method is explicit, i.e. the solution ![](http://latex.codecogs.com/gif.latex?y_%7Bn&plus;1%7D)is an explicit function of ![](http://latex.codecogs.com/gif.latex?y_%7Bi%7D) for ![](http://latex.codecogs.com/gif.latex?i%5Cleqslant%20n)<br> While the Euler method integrates a first-ordr ODE, any ODE of order N can be represented as a first-order ODE:to treat the equation<br> ![](http://latex.codecogs.com/gif.latex?y%5E%7B%28N%29%7D%28t%29%3Df%28t%2Cy%28t%29%2Cy%27%28t%29%2C...%2Cy%5E%7B%28N-1%29%7D%28t%29%29)<br> We introduce auxiliary variables ![](http://latex.codecogs.com/gif.latex?z_%7B1%7D%28t%29%3Dy%28t%29%2Cz_%7B2%7D%28t%29%3Dy%27%28t%29%2C...%2Cz_%7BN%7D%28t%29%3Dy%5E%7B%28N-1%29%7D%28t%29%29) and obtain the equivalent equation<br>![](http://latex.codecogs.com/gif.latex?%5Cvec%7Bz%7D%27%28t%29%3D%5Cbegin%7Bpmatrix%7D%20z%27_1%28t%29%5C%5C%20...%5C%5C%20z%27_%7BN-1%7D%28t%29%5C%5C%20z%27_N%28t%29%20%5Cend%7Bpmatrix%7D%3D%5Cbegin%7Bpmatrix%7D%20y%27%28t%29%5C%5C%20...%5C%5C%20y%5E%7B%28N-1%29%7D%28t%29%5C%5C%20y%5E%7B%28N%29%7D%28t%29%20%5Cend%7Bpmatrix%7D%3D%5Cbegin%7Bpmatrix%7D%20z_2%28t%29%5C%5C%20...%5C%5C%20z_N%28t%29%5C%5C%20f%28t%2Cz_1%2C...%2Cz_N%29%20%5Cend%7Bpmatrix%7D)<br>This is a first order system in the variable z and can be handled by Euler's method.


* Drag Force of air：<br>
The physisc of air resistance is a very complicated problem. In general, this force can be wirten as<br>![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-B_1v-B_2v%5E2)
At extremly low velocities the first term dominates, and its coefficient B1 can be calculated for objects with symple shapes. This is known as Stokes' law and is considered in most elementary texts. However, at any reasonable velocity the second term dominates for most objects. Moreover, B2 cannot be calculated exactly for objects even as symple as baseball. We can, however, approximately estimate B2 as follows. As an object moves through the atmosphere, it must push the air in front of it out of the way. The mass of air moved in time dt in ![](http://latex.codecogs.com/gif.latex?m_%7Bair%7D%5Csim%20%5Crho%20Avdt),where ![](http://latex.codecogs.com/gif.latex?%5Crho) is the density of air and A the frontal area of the object. This air is then given a velocity of order v, and hence its kinetic energy is ![](http://latex.codecogs.com/gif.latex?E_%7Bair%7D%5Csim%20m_%7Bair%7Dv%5E2/2). This is also the work done by the drag force (the force on the object due to air resistance) in time dt, so ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7Dvdt%3DE_%7Bair%7D). Putting this all together, we get<br> ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-%5Cfrac%7B1%7D%7B2%7DC%5Crho%20Av%5E2)


* Two approach to estimate the desity variation of air: <br>Anothor factor influencing air resistance in this problem is the variation of air density. During this process, the shell travels to a very high altitude, where the air density will be lower than sea level. As is discussed above, the air resistance is proportional to the density of the air, so the drag force at high altitude will be less than that at sea level.
  * Isothermal: In this approach, the air is treated as an isothermal ideal gas. Then the pressure p depends on alititude according to<br>![](http://latex.codecogs.com/gif.latex?p%28y%29%3Dp%280%29e%5E%7B-mgy/k_BT%7D)<br>where m is the avarage mass of an air molecule, y is the height from some reference point (say, the sealevel), ![](http://latex.codecogs.com/gif.latex?k_B)is the Boltzmann's constant, and T is the absolute temperature. For an ideal gas the pressure is propotional to the density, so this leads to<br> ![](http://latex.codecogs.com/gif.latex?%5Crho%20%3D%5Crho%20_0e%5E%7B-y/y_0%7D)<br>where ![](http://latex.codecogs.com/gif.latex?y_0%20%3Dk%20_BT/mg%5Capprox%201.0%5Ctimes%2010%5E4m)and ![](http://latex.codecogs.com/gif.latex?%5Crho%20_0) is the density at sea level(y=0)<br>This isothermal model of the atmosphere is perhaps not very realistic, since we know that the air temprature varies quite a bit over altitude changes of a few kilometers.
  * Adiabatic: This is a different approach to assume that the air is a poor conductor of heat, and that convection is very slow. This leads to the so-called adiabatic approximation, which is much better for the troposphere. The adiabatic approximation leads to a somewhat different dependence of the density on the altitude<br> ![](http://latex.codecogs.com/gif.latex?%5Crho%3D%5Crho%20_0%281-%5Cfrac%7Ba%20y%7D%7BT_0%7D%29%5E%5Calpha)<br>where ![](http://latex.codecogs.com/gif.latex?a%5Capprox%206.5%5Ctimes%2010%5E%7B-3%7DK/m) fits measured data fairly well. Here ![](http://latex.codecogs.com/gif.latex?T_0) is the sea level temperature (in K), and the exponent ![](http://latex.codecogs.com/gif.latex?%5Calpha%20%5Capprox%202.5) for air.
Whichever model of air density is used, however, the basic stratage of the numerical calculation is the same. And the drag force due to air resistance is proportional to the density, that is <br> ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5E%7B*%7D%3D%5Cfrac%7B%5Crho%20%7D%7B%5Crho%20_o%7DF_%7Bdrag%7D%28y%3D0%29)<br>where ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%28y%3D0%29) is the force at sea level, and ![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%5E%7B*%7D)is the drag at altitude.

## Methods
The Euler method is used to solve the equation of motion of the cannon shell, which is <br> ![](http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D%3DF_x%5C%5C%20%5Cfrac%7Bd%5E2y%7D%7Bdt%5E2%7D%3DF_y%20%5Cend%7Bmatrix%7D%5Cright.)<br> where x and yare horizontal and vertical coordinates of the projectile, and ![](http://latex.codecogs.com/gif.latex?F_x%2CF_y) depend on the approximations or corrections we made, i.e. 
* when we ignore air resistance, then <br> ![](http://latex.codecogs.com/gif.latex?F_x%3D0%2CF_y%3D-g)
* when air resistance is considered but the air is considered uniform, then <br> ![](http://latex.codecogs.com/gif.latex?F_x%3D-B_2vv_x%2CF_y%3D-g-B_2vv_y)
* when air resistance is considered and the air is considered isothemal, then <br> ![](http://latex.codecogs.com/gif.latex?F_x%3D-e%5E%7B-y/y_0%7DF_%7Bdrag%7D%28y%3D0%29vv_x%2CF_y%3D-g-e%5E%7B-y/y_0%7DF_%7Bdrag%7D%28y%3D0%29vv_y)
* when air resistance is considered and the air is considered adiabatic, then <br>![](http://latex.codecogs.com/gif.latex?F_x%3D-%281-%5Cfrac%7Bay%7D%7BT_0%7D%29%5E%7B%5Calpha%20%7DF_%7Bdrag%7D%28y%3D0%29vv_x%2CF_y%3D-g-%281-%5Cfrac%7Bay%7D%7BT_0%7D%29%5E%7B%5Calpha%20%7DF_%7Bdrag%7D%28y%3D0%29vv_y)<br>


In order to apply Euler method, we need to rewrite the equations as follow<br> ![](http://latex.codecogs.com/gif.latex?%5Cleft%5C%7B%5Cbegin%7Bmatrix%7D%20%5Cfrac%7Bdx%7D%7Bdt%7D%3Dv_x%5C%5C%20%5Cfrac%7Bdv_x%7D%7Bdt%7D%3DF_x%5C%5C%20%5Cfrac%7Bdy%7D%7Bdt%7D%3Dv_y%5C%5C%20%5Cfrac%7Bdv_y%7D%7Bdt%7D%3DF_y%20%5Cend%7Bmatrix%7D%5Cright.)<br> 


The landing point of the shell is determined by interpolating between the last point above the gound(n) and the point that would have been below the grounf (n+1). If we let ![](http://latex.codecogs.com/gif.latex?r%3D-y_n/y_%7Bn&plus;1%7D) then a linear interpolation gives <br> ![](http://latex.codecogs.com/gif.latex?x_l%3D%5Cfrac%7Bx_n&plus;rx_%7Bn&plus;1%7D%7D%7Br&plus;1%7D%2Cy_l%3D0)


## Results and discussions
* The influence brought about by air resistance<br> 





















