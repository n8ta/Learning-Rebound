# Lesson 4 - Simulation Archives

Another way to analyze rebound is using simulation archives. Simulation archives are binary files that store all the information about MULTIPLE states of a simulation. They can be used to save a state for example 1 year of a 100 year simulation so you can go back and inspect the data over time. Archives are also files so you can save them and look at their contents later unlike a script that runs once and then is no longer accessible.

You initialize (create) a simulation archive before you begin integrating using the initSimulationArchive() method of the simulation type.
```python
sim.initSimulationArchive("output.bin",interval_walltime=10)
```
initSimulationArhive has a few inputs, the first a string in quotes is the name of the output file in this case "output.bin". The next is how often the archive should be saved, walltime refers to clock time, this code will save a state every 10 seconds. You can also use interval=# to save every unit of time (in an earlier lesson we set units of years so this # would be in years.
```python
sim.initSimulationArchive("output.bin",interval=10)
```
This is equally valid as the earlier line.

