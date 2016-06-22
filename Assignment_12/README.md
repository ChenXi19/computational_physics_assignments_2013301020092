# Assignment_12 Hyperion

student name: CHEN XI<br>
student number: 2013301020092

## Abstract 
In this assignment, the motion of Hyperion will be discussed according to the instruction of Problem4.20.

## Introduction

* The Basic Information of Hyperion:

  Hyperion, also known as Saturn VII (7), is a moon of Saturn discovered by William Cranch Bond, George Phillips Bond and William Lassell in 1848. It is distinguished by its irregular shape, its chaotic rotation, and its unexplained sponge-like appearance. It was the first non-round moon to be discovered.<br>

  ![](https://upload.wikimedia.org/wikipedia/commons/9/94/Hyperion_true.jpg)

  The moon is named after Hyperion, the Titan god of watchfulness and observation – the elder brother of Cronus, the Greek equivalent of Saturn – in Greek mythology. It is also designated Saturn VII. The adjectival form of the name is Hyperionian.

  Hyperion's discovery came shortly after John Herschel had suggested names for the seven previously-known satellites of Saturn in his 1847 publication Results of Astronomical Observations made at the Cape of Good Hope. William Lassell, who saw Hyperion two days after William Bond, had already endorsed Herschel's naming scheme and suggested the name Hyperion in accordance with it. He also beat Bond to publication.<br>

* Rotation of Hyperion:

  The Voyager 2 images and subsequent ground-based photometry indicated that Hyperion's rotation is chaotic, that is, its axis of rotation wobbles so much that its orientation in space is unpredictable. Hyperion, together with Pluto's moons Nix and Hydra, is among only a few moons in the Solar System known to rotate chaotically, although it is expected to be common in binary asteroids. It is also the only regular planetary natural satellite in the Solar System known not to be tidally locked.

  Hyperion is unique among the large moons in that it is very irregularly shaped, has a fairly eccentric orbit, and is near a much larger moon, Titan. These factors combine to restrict the set of conditions under which a stable rotation is possible. The 3:4 orbital resonance between Titan and Hyperion may also make a chaotic rotation more likely. The fact that its rotation is not locked probably accounts for the relative uniformity of Hyperion's surface, in contrast to many of Saturn's other moons, which have contrasting trailing and leading hemispheres.

* Analysis of The Motion of Hyperion:

  There are two forces acting on each of the masses, the force of the gravity from Saturn and the force from the rod. Since we are interested in the motion about the center of mass, the force from the rod does not contribute. The gravitational force on m1 can be written as
  
  ![](http://latex.codecogs.com/gif.latex?%5Cvec%7BF%7D%3D-%5Cfrac%7BGM_%7Bsat%7Dm_1%7D%7Br_%7B1%7D%5E%7B3%7D%7D%28x_1%5Cvec%7Bi%7D&plus;y_1%5Cvec%7Bj%7D%29)
  
  where ![](http://latex.codecogs.com/gif.latex?M_%7BSat%7D) is the mass of Saturn, r1 is the distance from Saturn to m1, i and j are unit vectors in the x and y directions. The coordinates of the center of mass are (xc,yc), so that (x1-xc)i+(y1-yc)j is the vector from the center of mass  to m1. The torque on m1 is then 
  
  ![](http://latex.codecogs.com/gif.latex?%5Cvec%7Br_1%7D%3D%5B%28x_1-x_c%29%5Cvec%7Bi%7D&plus;%28y_1-y_c%29%5Cvec%7Bj%7D%5D%5Ctimes%20%5Cvec%7BF_1%7D)
  
  with a similar expression for r2. The total torque on the moon is just r1+r2 and this is related to the time derivative of ![](http://latex.codecogs.com/gif.latex?%5Comega) by:
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Cvec%7B%7D%5Comega%7D%7Bdt%7D%3D%5Cfrac%7B%5Cvec%7Br_1%7D&plus;%5Cvec%7Br_2%7D%7D%7BI%7D)
  
  where ![](http://latex.codecogs.com/gif.latex?I%3Dm_1r_1%5E2&plus;m_2r_2%5E2) is the moment of inertia. putting this all together yelds, after some algebra,
  
  ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Comega%7D%7Bdt%7D%3D-%5Cfrac%7B3GM_%7Bsat%7D%7D%7Br_c%5E5%7D%28x_csin%5Ctheta-y_ccos%5Ctheta%29%28x_ccos%5Ctheta&plus;y_csin%5Ctheta%29)
  
  where rc is the distance from the center of mass to Saturn.
  
## Result:
  
 * Circular Orbit:
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_circal_COM.png)

  Figure1.1: The motion of the center of mass in x-y pland

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_circal_m1m2.png)
  
  Figure1.2: The motion of m1 and m2 in the x-y plane 
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_circal_theta.png)
  
  Figure1.3: The pot of ![](http://latex.codecogs.com/gif.latex?%5Ctheta) of the Hyperion as a function of time t, when assuming the circular orbit, which is not chaotic. 
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_circal_omega.png)
  
  Figure1.4: The pot of ![](http://latex.codecogs.com/gif.latex?%5Comega) of the Hyperion as a function of time t, when assuming the circular orbit, which is not chaotic. 
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_circal_dtheta.png)
  
  Figure1.5: The pot of ![](http://latex.codecogs.com/gif.latex?%5CDelta%20%5Ctheta) of the Hyperion as a function of time t, when assuming the circular orbit, which is not chaotic. 
  
  
* Elliptical orbit

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_eliptical_COM.png)

  Figure2.1: The motion of the center of mass in x-y pland

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_eliptical_m1m2.png)
  
   Figure2.2: The motion of m1 and m2 in the x-y plane 
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_eliptical_theta.png)
  
  Figure2.3: The pot of ![](http://latex.codecogs.com/gif.latex?%5Ctheta) of the Hyperion as a function of time t, when assuming the elliptical orbit, which is chaotic.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_eliptical_omega.png)
  
  Figure2.4: The pot of ![](http://latex.codecogs.com/gif.latex?%5Comega) of the Hyperion as a function of time t, when assuming the elliptical orbit, which is chaotic.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_12/figure_eliptical_dtheta.png)
  
  Figure2.5: The pot of ![](http://latex.codecogs.com/gif.latex?%5CDelta%20%5Ctheta) of the Hyperion as a function of time t, when assuming the elliptical orbit, which is chaotic.
  
* Conclusion:
  
  The motion of the Hyperion is not chaotic when we assume the circular orbit, while it becomes chaotic when the orbit is elliptical.

* Source Code:
  ![For source code please click here](https://github.com/ChenXi19/computational_physics_assignments_2013301020092/blob/master/Assignment_12/untitled1.py)

## Reference:

[1] ![The Hyperion on wiki](https://en.wikipedia.org/wiki/Hyperion_(moon))

[2] The source code is modified from that of Qiang Yihua.

