# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:29:32 2023

@author: Shikhar Krishn Jha
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define parameters
t = np.linspace(0, 2 * np.pi, 1000)  # Parameter from 0 to 2*pi

# Define the parametric equations for the trefoil knot
def trefoil_knot(t):
    x = np.sin(t) + 2 * np.sin(2 * t)
    y = np.cos(t) - 2 * np.cos(2 * t)
    return x, y

# Create a figure and axis
fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)

# Customize the plot (optional)
ax.set_title("Trefoil Knot Animation")
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)

# Initialize the plot
def init():
    line.set_data([], [])
    return line,

# Update the plot for each frame of the animation
def update(frame):
    x, y = trefoil_knot(frame)
    line.set_data(x, y)
    return line,

# Create the animation
ani = FuncAnimation(fig, update, frames=t, init_func=init, blit=True, interval=20)

# Display the animation
plt.show()
