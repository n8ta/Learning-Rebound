# Lesson 2 - Setting up a Rebound Simulation
## Lesson 2 Video
[![Alt text](/L2.png)](https://www.youtube.com/watch?v=7z-6_2lDpH0&feature=youtu.be)
## Simulations
Using the code from Lesson 1 that generated initial conditions we will create a rebound simulation with those two objects.
We will be assuming these initial values are know in this lesson:
```python
# Constants
G = 39.43163873354829472
M1 = 1
M2 = 10
q1 = M1/M2
q2 = M2/M1
e=0
a=5
# Generation Initial Conditions
RadiusOfM1 = (1.0-e)*a/(1.0+q1)
VelocityOfM1 = (G*(M1+M2)/a)**.5 * (((1.0+e)/(1.0-e)))**.5 / (1.0+q1)
RadiusOfM2 = (1.0-e)*a/(1.0+q2)
VelocityOfM2 = (G*(M1+M2)/a)**.5 * (((1.0+e)/(1.0-e)))**.5 / (1.0+q2)
```

Rebound is a module, that said you must import it into python:
```python
import rebound
```

Now we can access of all the rebound.METHODS which are the core of rebound. For starters lets create a simulation object. A simulation object holds all the bodies and their properties in a simulation. You can find all rebound methods here: https://rebound.readthedocs.io/en/latest/python_api.html in rebounds own robust documentation.
```python
sim = rebound.Simulation()
```
Note: 'sim' is just the name of the object we created to store the rebound Simulation object, it could be called anything. 

Next we set the units so Rebound knows how to interpret our inputs. We do this by setting the value of sim.units, sim.units is not a method but a public variable that we can edit. Methods do things, variables store things. 

```python
sim.units = ('yr', 'AU', 'Msun')
```
You don't need to use years AU and Msun but I like them because they keep our numbers small and managable.

Next we add our objects to the simulation using the sim.add method. The method accepts inputs of mass (m) xposition (x) yposition (y) zposition (z) xvelocity (vx) etc.

```python
sim.add(m=M1, x=-r1, y=0, z=0, vx=0, vy=-V1, vz=0)
sim.add(m=M2, x=r2, y=0, z=0, vx=0, vy=V2, vz=0)
```
Notice M1 is given a negative x position, this is because it is at the far left of its orbit, M2 has a positive xposition so that it is at the far right position of the orbit. The velocities are also opposite as in all binary systems. All z values are set to 0 as this simulation takes place in the x-y plane. You could easily tile it using trigfunctions / vector components but that is out of the scope of this tutorial.

Now we've created our simulation added our objects, we need to set the time, general t=0 is used.
```python
sim.t = 0
```
sim.t isn't a method it doesn't end in () like sim.add and sim.units, it's a value that we are setting. sim.add is more complicated and thus needs its own function to all the behind the scenes work of initializing bodies.

Finally we run our simulation, this is commonly called 'integrating' and you again use a method of the sim object. We need to set a time to integrate until so we declare a tmax variable (max time) and pass it into the integrate function. You could easily just input a number but I prefer to declare a variable so I can access it other places if necessary.
```python
tmax = 10
sim.integrate(tmax)
```
The simulation will then run until completion. This can sometimes take awhile, the following increase the time for the simulation to finish:
- Number of bodies (more bodies take more time than fewer)
- Speed of bodies (faster takes more time than slower)
- Closeness of bodies (closer takes more time than farther)

[Continue to Lesson 3](https://github.com/UncleIroh/Learning-Rebound/blob/master/Lesson3.md)
