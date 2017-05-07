# Lesson 5 Matplotlib Basics
## Lesson 5 Video
[![Alt text](/L5.png)](https://www.youtube.com/watch?v=Ziq7v-2wTSY)
## Importing Libraries
Matplotlib is a library for python that has a lot of graphing tools. We're also going to import numpy (a math calculation library, adds sin,cos,sqrt, and others). Adding "as" after importing changes the name to reference the library. So numpy.sin() becomes np.sin() when you import as np.
```python
import matplotlib.pyplot as plt
import numpy as np
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
The pyplot (plt) methods for modifying axes limits are .ylim(ymin,ymax) and .xlim(xmin,xman). Be careful when setting limits it can make importance data not visible, it's best to take a broad view and only set limits manually when you are sure you know what is going on. To add a title to your graph use the .title() method, it accepts a string as do .xlabel() and .ylabel() which label the x and y axes.
```python 
import numpy as np
import matplotlib.pyplot as plt
xlist = np.arange(.5,5,.1) #creates a list from .5 to 5 by increments of .1
ylist = np.sin(xlist)
plt.plot(xlist,ylist,"ro",markersize=6)
#plt.xlim(1,4) 
#plt.ylim(-1,1)
#plt.title("This graph has bounds of [1,4]x[-1,1]")
#plt.xlabel("This is the xaxis")
#plt.ylabel("This is the yaxis")
plt.show()

```
Below are two images one without the commented lines and one with so you can see the difference with and without limits/titles.
![Comparison](https://raw.githubusercontent.com/UncleIroh/Learning-Rebound/master/comp.png)

Final note for matplotlib, sometimes your axes can make your images looked warped. I recommend adding:
```python
plt.axis('equal')
```
to every plot that has positions on the and x y axes, on time vs anything plots this is not necessary.

[Continue to Lesson 6](/Lesson6.md) 
