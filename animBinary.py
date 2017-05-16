import rebound
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
sa = rebound.SimulationArchive("output.bin")
print(sa.tmax)
time = np.arange(0,sa.tmax,.01)
M1xpos = []
M1ypos = []
M2xpos = []
M2ypos = []
M3xpos = []
M3ypos = []
M4xpos = []
M4ypos = []

for item in time:
    #print(item)
    sim = sa.getSimulation(t=item)
    M1xpos.append(sim.particles[0].x)
    M1ypos.append(sim.particles[0].y)
    M2xpos.append(sim.particles[1].x)
    M2ypos.append(sim.particles[1].y)
    M3xpos.append(sim.particles[2].x)
    M3ypos.append(sim.particles[2].y)
    M4xpos.append(sim.particles[3].x)
    M4ypos.append(sim.particles[3].y)


skip = 20
def animate(i):
    z = i * skip
    ax.clear()
    #axes = plt.gca()
    plt.xlim(-40,40)
    plt.ylim(-40,40)
    c=10
    plt.plot(M1xpos[z],M1ypos[z],'bo',markersize=c)
    plt.plot(M2xpos[z],M2ypos[z],'bo',markersize=c)
    plt.plot(M3xpos[z],M3ypos[z],'bo',markersize=c)
    plt.plot(M4xpos[z],M4ypos[z],'bo',markersize=c)

fig = plt.figure(figsize=(6,6))
fig.subplots_adjust(left=.12, bottom=.1, right=.96, top=.9, wspace=.20, hspace=.27)
ax = fig.add_subplot(111)
ani = animation.FuncAnimation(fig, animate, interval=1, frames=int((len(time)/skip)), repeat=False)
plt.show()
