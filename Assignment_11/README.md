# Assignment_11 Kepler's Law and The Binary System

student name: CHEN XI<br>
student number: 2013301020092

## Abstract 

In this assignment, the different motions of two planets as a binary system will be discussed with respect to different mass ratio. Also the motions of Earth orbiting around sun will be discussed under different initial velocities.

## Introduction

* Kepler's Law
  
  In astronomy, Kepler's laws of planetary motion are three scientific laws describing the motion of planets around the Sun.

  ** The orbit of a planet is an ellipse with the Sun at one of the two foci.
  ** A line segment joining a planet and the Sun sweeps out equal areas during equal intervals of time.
  ** The square of the orbital period of a planet is proportional to the cube of the semi-major axis of its orbit.

  ![](https://upload.wikimedia.org/wikipedia/commons/9/98/Kepler_laws_diagram.svg)<br>
  Figure 1: Illustration of Kepler's three laws with two planetary orbits.

  Most planetary orbits are close to being circles, and careful observation and calculation is required in order to establish that they are actually not perfectly circular ellipses. Using calculations of the orbit of Mars, whose published values are somewhat suspect, which indicated elliptical orbits, Johannes Kepler inferred that other heavenly bodies, including those farther away from the Sun, also have elliptical orbits.

  Kepler's work (published between 1609 and 1619) improved the heliocentric theory of Nicolaus Copernicus, explaining how the planets' speeds varied, and using elliptical orbits rather than circular orbits with epicycles[3]

  Isaac Newton showed in 1687 that relationships like Kepler's would apply in the solar system to a good approximation, as consequences of his own laws of motion and law of universal gravitation.

  Kepler's laws are part of the foundation of modern astronomy and physics.


* Newton's Law of Gravitation
  
  By Newton's second law, the gravitational force that acts on the planet is:
  
  ![](http://latex.codecogs.com/gif.latex?%5Cvec%7BF%7D%3Dm_%7Bplanet%7D%5Cddot%7B%5Cvec%7Br%7D%7D%3D-m_%7Bplanet%7D%5Calpha%20r%5E%7B-2%7D%5Cvec%7Br%7D)

  wherewhere ![](http://latex.codecogs.com/gif.latex?m_%7Bplanet%7D) is the mass of the planet and α has the same value for all planets in the solar system. According to Newton's third Law, the Sun is attracted to the planet by a force of the same magnitude. Since the force is proportional to the mass of the planet, under the symmetric consideration, it should also be proportional to the mass of the Sun, ![](http://latex.codecogs.com/gif.latex?m_%7BSunt%7D). So
  
  ![](http://latex.codecogs.com/gif.latex?%5Calpha%3DGm_%7BSun%7D)
  
  where G is the gravitational constant.

  The acceleration of solar system body number i is, according to Newton's laws:
  
  ![](http://latex.codecogs.com/gif.latex?%5Cddot%7B%5Cvec%7Br_i%7D%7D%3DG%5Csum%7Bm_jr_%7Bij%7D%5E%7B-2%7D%5Cvec%7Br_%7Bij%7D%7D%7D)
  
  where ![](http://latex.codecogs.com/gif.latex?m_%7Bj%7D) is the mass of body j,![](http://latex.codecogs.com/gif.latex?r_%7ij%7D) is the distance between body i and body j, ![](http://latex.codecogs.com/gif.latex?%5Cvec%7Br_%7Bij%7D%7D%7D) is the unit vector from body i towards body j, and the vector summation is over all bodies in the world, besides i itself.

  In the special case where there are only two bodies in the world, Earth and Sun, the acceleration becomes
  
  ![](http://latex.codecogs.com/gif.latex?%5Cddot%7B%5Cvec%7Br%7D%7D_%7BEarth%7D%3DG%7Bm_%7BSun%7Dr_%7BEarth%2CSun%7D%5E%7B-2%7D%5Cvec%7Br%7D_%7BEarth%2CSun%7D)
  
  
* Binary System
  
  A binary system is a system of two objects in space (usually stars, but also brown dwarfs, planets, neutron stars, black holes, galaxies, or asteroids) which are close enough that their gravitational movement causes them to circle around each other (orbit) around a shared mass. Some definitions (e.g. that of double planet, but not that of binary star) require that this center of mass is not located within the interior of either object. A multiple system is like a binary system but consists of three or more objects.

  ![](https://upload.wikimedia.org/wikipedia/commons/6/6c/Pluto-Charon_System.gif)<br>
  Figure_2 Pluto and its moon Charon are often described as a binary system.
  
## Results

* Motions of Binary System With Different Mass Ratio
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_11/1.png)<br>Figure3.1 The motion of a binary system with a mass ratio being 1.

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_11/2.png)<br>Figure3.2 The motion of a binary system with a mass ratio being 2.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_11/3.png)<br>Figure3.3 The motion of a binary system with a mass ratio being 3.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_11/10.png)<br>Figure3.4 The motion of a binary system with a mass ratio being 10.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_11/1042.png)<br>Figure3.5 The motion of a binary system with a mass ratio being 1042.
  
  Colusion:
  
  (1) When the mass ratio gets larger and larger, the orbits of the planet with a larger mass becomes smaller and smaller. 
  
  (2) When the mass of one planet is far larger than the other planet, the heavier planet can be treated as still with the lighter planet orbiting around. And hence when analysing the motion of the Earth, we can treat the sun as still with Earth orbiting around the sun.
  
  
  ![For Source Code Please Click](https://github.com/ChenXi19/computational_physics_assignments_2013301020092/blob/master/Assignment_11/111.py)
* Orbits of Earth Under Different Initial Velocity
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_11/v1.png)<br> Figure4.1 The orbit of Earth with initial velocity being 1.

  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_11/v2.png)<br> Figure4.2 The orbit of Earth with initial velocity being 2.
  
  ![](https://raw.githubusercontent.com/ChenXi19/computational_physics_assignments_2013301020092/master/Assignment_11/v3.png)<br> Figure4.3 The orbit of Earth with initial velocity being 3.
  
  From the above figures, we can conclude that the shape of the orbit of Earth is dependent of its initial velocity.
  
  ![For Source Code Please Click](https://github.com/ChenXi19/computational_physics_assignments_2013301020092/blob/master/Assignment_11/112.py)
  
  
## Reference

[1]![Kepler's laws of planetary motion on Wikipedia](https://github.com/ChenXi19/computational_physics_assignments_2013301020092/tree/master/Assignment_12) 

[2]![Binary system on Wilipedia](https://en.wikipedia.org/wiki/Binary_system)

[3]Source code is from Liu Wentao.
