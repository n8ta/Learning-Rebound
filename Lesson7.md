# Lessons 7 - Animating Rebound Data

## Lessons 7 Videos
[![Alt text](/L6.png)](https://www.youtube.com/watch?v=iiFHiK4mug0)

## Animating
We are going to be using matplotlib.animation.FuncAnimation to animate our data. This method creates an an animation that runs a function every interval=# milliseconds for frames=# of frames. You begin by creating your matplotlib figure, I'll be using a 6x6 figure. I also adjust some of the properties of the figure with fig.subplots_adjust to make sure all axes labels are readable. You can play with these options by clicking this button in any matplotlib plot.
![button](/button.jpg)
```python
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(6,6))
fig.subplots_adjust(left=.12, bottom=.1, right=.96, top=.9, wspace=.20, hspace=.27)
```

