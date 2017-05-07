# Lesson 3 - Analyzing Rebound Data
## Lesson 3 Video
[![Lesson3Video](/L31.png)](https://www.youtube.com/watch?v=yKZ5OdaZPiI)
## Quantitative Energy Analysis
There are two many ways to analyze data, quanitatively (numerically) and qualitatively (visually in this context). We'll begin with the quanitative analysis becuase it is more straightforward to extract numberes than images from a simulation.

The most important way we measure a simulation is it's (Ef-E0)/E0 where Ef=Energy Final & E0=Energy Initial, the percentage chagne in energy. Ideally this value is sub 10^-8, but sub 10^-4 is sometimes acceptable. Rebound handles making sure your simulation conserves energy by slowing timesteps and even recalculating timesteps when energy errors are too large, this can slow down your simulations but a slower simulation is better than one with useless results.

To calculate (Ef-E0)/E0 you need to store your initial energy at the beginning of the simulation, this is done with the simulation method.
```python
E0 = sim.calculate_energy()
```
You would run this line at the beginning of your simulation and print/store it at the end.

After your simulation has run or at any time during it) you would run calc energy again.
```python
E0 = sim.calculate_energy() 
sim.integrate(tmax)
Ef = sim.calculate_energy() 
print("(Ef-E0)/E0 = "+(E0+Ef)/E0)
```

### A Sidenote on Strings and Python
A quick note on printing/concatonation (combining):
To print in python type print() you can put variables like E0 in the () to print them, you can also chain text (strings is the technical term) with variables using the + operator. Remember strings go in "" and variables do not.

After this runs we will receive a printout something like:
```
(Ef-E0)/E0 = .000000342394
```
## Accessing Variables and Methods of Classes (like the particles class)
Another way to get information from the simulation is to access particles objects within the simulation object.
```
planet0 = sim.particles[0]
print(planet0.vx,planet0.vy,planet0,vz)
```

planet0.vx calls the vx variable of the planet0 object (of type rebound.simulation.particles). You can extract the following variables from particle objects. They will return the values at current integration (time) of the simulation. If you want older various you need to save them periodicly this will be covered next.

- positions: x,y,z
- velocities: vx,vy,vz
- accelerations: ax,ay,az
- mass: m
- radius: r (usually user defined not necessary for simulations without collisions)
- last collision: lastcollision (time of last collisions)
- various C pointers, rebound is built on C and so python objects are just wrappers for C objects, these variables return the C pointers (pointers point to a location in system memory (RAM) where an object is stored)

One useful method of the particels object is the .calculate_orbit() method. It requires another particle as input and returns an orbit object with all orbital parameters.
```python
p0 = sim.particles[0]
p1 = sim.particles[1]
orbit = p0.calculate_orbit(p1)
print(orbit.e)
```
You can find a full list of orbital parameters like eccentricity (e) [here](https://rebound.readthedocs.io/en/latest/python_api.html#rebound.Orbit)

[Continue to Lesson 4](/Lesson4.md)
