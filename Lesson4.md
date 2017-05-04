# Lesson 4 - Simulation Archives

Another way to analyze rebound is using simulation archives. Simulation archives are binary files that store all the information about MULTIPLE states of a simulation. They can be used to save a state for example 1 year of a 100 year simulation so you can go back and inspect the data over time. Archives are also files so you can save them and look at their contents later unlike a script that runs once and then is no longer accessible. 

Archives can also be accessed while simulations are still running, this is incredibly useful for simulations that run for long periods of time so you can check to make sure they are still working correctly.

You initialize (create) a simulation archive before you begin integrating using the initSimulationArchive() method of the simulation type.
```python
sim.initSimulationArchive("output.bin",interval_walltime=10)
```
initSimulationArhive has a few inputs, the first a string in quotes is the name of the output file in this case "output.bin". The next is how often the archive should be saved, walltime refers to clock time, this code will save a state every 10 seconds. You can also use interval=# to save every unit of time (in an earlier lesson we set units of years so this # would be in years unlike walltime which is always in seconds.
```python
sim.initSimulationArchive("output.bin",interval=10)
```

To access simulations archives we use the .simulationArchive method of rebound. This method requires one input the name of the file to open. The SimulationArchive method returns a simulation archive object which in turn has methods. The most importance method of the archive object is its .getSimulation(t=x) method which returns a simulation object with all particles at time x. If time x isn't close to a snapshot at which you saved (based on the interval) it may take time for rebound to integrate to that point.
```python
archive = rebound.SimulationArchive("output.bin")
sim1 = archive.getSimulation(t=1)
```
By extracting info from simulations, basic lists, and the matplotlib (graphing) library we can create graphs of our particles locations/velocities/energy over time.

[Continue to Lesson 5](https://github.com/UncleIroh/Learning-Rebound/edit/master/Lesson5.md)
