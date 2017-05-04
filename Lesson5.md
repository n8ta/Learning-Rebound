# Lesson 5 Matplotlib Basics

Matplotlib is a library for python that has a lot of graphing tools. To import the pyplot module of matplotlib type:
```python
import matplotlib.pyplot as plt
```
Now when we type plt.show() that will be equivalent to matplotlib.pyplot.show(), this is just to save time. The key method of pyplot (or plt as we will be calling it) is .plot(). .plot() accepts two lists and a marker type. The first list is the xcords of xy cords and the second list of a list of y cords. The marker type is how the pts appear on the graph.

Marker types are a combination of color code and shape code, colors are red (r) green (g) blue (b) and others and shapes are circle (o) cross (+) hexagon (h). There are tons of these shapes/colors read about that [here](https://matplotlib.org/api/markers_api.html#module-matplotlib.markers). This prints the points (1,1) (2,4) and (3,9) with red hexagons.
You can also change the marker size by adding the markersize=# argument to the .plot method.

```python
plt.plot([1,2,3],[1,4,9],'rh',markersize=40)
plt.show()
```
![matplotlib graph](https://github.com/UncleIroh/Learning-Rebound/blob/master/fig.png?raw=true)

Next let's leanrn about axes, the key elements are labels, tick marks, titles, and bounds.
```python
import numpy
plt.plot(np.arange(.5,5,.1) #creates a list from .5 to 5 by increments of .1
