# Lessons 7 - Animating Rebound Data

## Lessons 7 Videos
[![Alt text](/L6.png)](https://www.youtube.com/watch?v=iiFHiK4mug0)

## Animating
We are going to be using matplotlib.animation.FuncAnimation to animate our data. This method creates an an animation that runs a function every interval=# milliseconds for frames=# of frames. You begin by creating your matplotlib figure, I'll be using a 6x6 figure. I also adjust some of the properties of the figure with fig.subplots_adjust to make sure all axes labels are readable. You can play with these options by clicking this button in any matplotlib plot and then adjusting your code to match.

![button](/button.jpg)
```python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(6,6))
fig.subplots_adjust(left=.12, bottom=.1, right=.96, top=.9, wspace=.20, hspace=.27)
```

We also need to create our axes, we haven't always done this in the past because we let matplotlib handle the axes as we didn't need to adjust them. To create an axis object.

```python
ax = fig.add_subplot(111)
```
The 111 refers to the # of rows, # of columns, # which plot you are refering to from left to right top to bottom. So if you added 221 and 223) you would get the top left of a 2x2 and the bottom left of a 2x2. This is useful if you want to create multiple plots in the same figure. To switch between plots you are motifying 
```python
plt.subplot(211)
plt.plot([1],[1],'bo')
plt.subplot(212)
plt.plot([2],[2],'ro')
```
In this case plt.subplot() chagnes your active subplot plots and then changes again. We won't be using subplots in this tutorial but everything we do could be done in subplots.

So to create our animation object we use matplotlib.animation.FuncAnimation
```
ani = matplotlib.animation.FuncAnimationfig, animate, interval=10, frames=len(time), repeat=False)
```
fig is the name of the figure we created earlier, animate is the name of a function that we have no created yet, it acceps the variable i (for iteration), frames gives the number of frames to animate (I use the length of the list without time values), and repeate is obvious.

So now we need to create the animate function to update the plot 
```python
def animate(i):
    ax.clear()
    plt.xlim(-40,40) # Make sure you set limits that show everything, you may see a blank plot if you have bad limits.
    plt.ylim(-40,40) # Set the limits in each frame because they are cleared by ax.clear()
    plt.plot(M1xpos[i],M1ypos[i],'bo',markersize=10)
```
This is assuming you have lists called M1xpos and M1ypos with values from a simulaton. If your animation is going to slowly you can either decrease your interval (keep it >1ms) or start skipping frames. You do this by instead of grabbing x/y positions at index i eg. M1xpos[i], you can grab them at M1xpos[4i] using in intermediate variable like this.
```python
skip = 4
def animate(i):
    z = i * 4
    ax.clear
    plt.xlim(-40,40)
    plt.ylim(-40,40) 
    plt.plot(M1xpos[z],M1ypos[z],'bo',markersize=10)
```
Making the skip number larger will skip frames. If you use a skip you will need to divide your frames=x by skip when you create the FuncAnimation so you don't keep animating after you run out of data.

Putting it all together we woud have one file called Binary.py and another called AnimBinary.py. Here are example files for a double binary I created (a binary orbitting a binary) it incorporates everything we did just for more masses and it applys the initial condition generation we learned twice once for the small and once for the large binaries.
![binary.py](/binary.py )
![animBinary.py](/animBinary.py )
