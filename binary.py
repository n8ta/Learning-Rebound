import rebound
import numpy as np
# Constants
G = 39.43163873354829472 #I'll explain why this isn't 6.67e-11 later
M1 = 1
M2 = 1
M3 = 1
M4 = 1
q = 1
a=5
a2=70
e=0
# Generation Initial Conditions
r1 = (1.0-e)*a/(1.0+q)
v1 = (G*(1+1)/a)**.5 * (((1.0+e)/(1.0-e)))**.5 / (1.0+q)
bigr1 = (1.0-e)*a2/(1.0+q)
bigv1 = (G*(4)/a2)**.5 * (((1.0+e)/(1.0-e)))**.5 / (1.0+q)

sim = rebound.Simulation()
sim.units = ('yr','AU','Msun')
sim.t = 0
tmax = 1000
sim.add(m=1,x=(bigr1+r1),y=0,z=0,vx=0,vy=(bigv1-v1),vz=0)
sim.add(m=1,x=(bigr1-r1),y=0,z=0,vx=0,vy=(bigv1+v1),vz=0)
sim.add(m=1,x=(-bigr1+r1),y=0,z=0,vx=0,vy=(-bigv1-v1),vz=0)
sim.add(m=1,x=(-bigr1-r1),y=0,z=0,vx=0,vy=(-bigv1+v1),vz=0)
sim.initSimulationArchive("output.bin",interval=.01)
sim.integrate(tmax)
