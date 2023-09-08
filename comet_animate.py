# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:05:11 2023

@author: Shikhar Krishn Jha
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define the initial position and velocity of the comet
x0, y0 = 0, 0
vx0, vy0 = 1, 1

# Define the time steps and number of frames
dt = 0.01
n_frames = 100

# Create an empty array to store the comet's positions
x = np.zeros(n_frames)
y = np.zeros(n_frames)

# Iterate over the time steps and update the comet's position
for i in range(n_frames):
    x[i] = x0 + vx0 * dt
    y[i] = y0 + vy0 * dt

    vx0 -= 0.01 * y[i]
    vy0 += 0.01 * x[i]

# Create the animation
fig, ax = plt.subplots()
line, = ax.plot([], [])

# need to sync with vscode
def animate(i):
    line.set_data(x[:i], y[:i])
    return line,

ani = animation.FuncAnimation(fig, animate, interval=100, frames=n_frames)

plt.show()
