# Lesson 3 - Analyzing Rebound Data

There are two many ways to analyze data, quanitatively (numerically) and qualitatively (visually in this context). We'll begin with the quanitative analysis becuase it is more straightforward to extract numberes than images from a simulation.

The most importance way we measure a simulation is it's (Ef-E0)/E0 where Ef=Energy Final & E0=Energy Initial, the percentage chagne in energy. Ideally this value is sub 10^-8, but sub 10^-4 is sometimes acceptable. Rebound handles making sure your simulation conserves energy by slowing timesteps and even recalculating timesteps when energy errors are too large, this can slow down your simulations but a slower simulation is better than one with useless results.

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
A quick note on printing/concatonation (combining):
To print in python type print() you can put variables like E0 in the () to print them, you can also chain text (strings is the technical term) with variables using the + operator. Remember strings go in "" and variables do not.

After this runs we will receive a printout something like:
```
(Ef-E0)/E0 = .000000342394
```

Another way to get information from the simulation is to access particles objects within the simulation object.
```
planet0 = sim.particles[0]
# Planet0 is now a particle object
print(planet0.vx,planet0.vy,planet0,vz)
# , is just like + it just adds space inbetween
