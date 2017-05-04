# Lesson 6 - Graphing Rebound Data with Matplotlib

Okay next up we combine the graphing skills we learned with matplotlib to rebound data. To do this we are going to have to learn some more advanced python to automate this process. We'll be working with this simulation/archive:
```python
import rebound
G = 39.43163873354829472
M1 = 0.000003002513826
M2 = 1
q1 = M1/M2
q2 = M2/M1
e=.4
a=1
radiusEarth = (1.0-e)*a/(1.0+q1)
velocityEarth = (G*(M1+M2)/a)**.5 * (((1.0+e)/(1.0-e)))**.5 / (1.0+q1)
radiusSun = (1.0-e)*a/(1.0+q2)
velocitySun = (G*(M1+M2)/a)**.5 * (((1.0+e)/(1.0-e)))**.5 / (1.0+q2)
sim = rebound.Simulation()
sim.units = ('yr', 'AU', 'Msun')
sim.add(m=M1, x=radiusEarth, y=0, z=0, vx=0, vy=velocityEarth, vz=0)
sim.add(m=M2, x=-radiusSun, y=0, z=0, vx=0, vy=-velocitySun, vz=0)
sim.t = 0
tmax = 1
sim.initSimulationArchive("output.bin",interval=.05)
sim.integrate(tmax)
```
This is a simulation of the Earth/Sun orbit with a higher than normal ecc.
Next we are going to extract data from this archive and store it in lsits to be graphed with matplotlib. We will create a dummy variable z and increment as we move forward through time. We are going to use a for loop, a for loop is a loop that repeats its code for each item in a list/array. Within the for loop you can access the current item in the list with whatever name you assign after "for". In this case I use "item" it could be anything.
```
dummyVar = [1,2,3,4]
for item in dummyVar:
  print(item*2)
```
This returns 1,4,6,8.
Now we will apply this principle to get data through tmax. We will use np.arange to again generate a list of time we want to sample and then get simulation data for each time. We will create empty lists for the x and y positions of the earth and sun and put data in each. With these we can create plots of their positions at various times. You create an empty list like this: x = []. We also are going to import the simulation archive.

So here are the lists we are going to fill:
```python
time = np.arange(0,1,.1)
earthXpos = []
earthYpos = []
earthV = []
sunXpos = []
sunYpos = []
sa = rebound.SimulationArchive("output.bin")
```
Next we fill the lists positions with a for loop based on the time list. To get total velocity you use the pythagoreaon theorem to combine the vx and vy velocities.
```python
for item in time:
    sim = sa.getSimulation(t=item)
    earthXpos.append(sim.particles[0].x)
    earthYpos.append(sim.particles[0].y)
    earthVX = sim.particles[0].vx
    earthVY = sim.particles[0].vy
    earthV = (earthVX**2+earthVY**2)**.5
    sunXpos.append(sim.particles[1].x)
    sunYpos.append(sim.particles[1].y)
```
Now for each time in our list we get a new simulation at the time "item" which refers to an entry in the time list and extract position data from it. We could easily get eccentricity info, velocities, accelerations, anything we can get from a normal simulation inside this for loop.

So let's inspect these lists by plotting them, make sure you have already
```python
import matplotlib.pyplot as plt
```
Now you let's take a look at the positions of the objects. Note this is showing all the the positions of the objects so we are seeing every snapshot 1/20yr all overlayed.
```python
plt.plot(sunXpos,sunYpos,'bo')
plt.plot(earthXpos,earthYpos,'ro')
plt.axis('equal')
plt.show()
```
This shows us the orbits on the scale the earth, because we haven't set axes it zooms out to show everything.
![EarthSunOrbit](https://github.com/UncleIroh/Learning-Rebound/blob/master/earthsunorbit.png)
