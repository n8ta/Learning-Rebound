# Lesson 6 - Graphing Rebound Data with Matplotlib

Okay next up we combine the graphing skills we learned with matplotlib to rebound data. To do this we are going to have to learn some more advanced python to automate this process. We'll be working with this simulation/archive:
```python
import rebound
G = 39.43163873354829472
M1 = 0.000003002513826
M2 = 1
q1 = M1/M2
q2 = M2/M1
e=0
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
This should be easily understood if you have completed the early lessons. It is an Earth/Sun orbit for a time of 1 year with snapshots saved at .01year intervals.
