# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 16:09:00 2023

@author: Shikhar Krishn Jha
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define parameters
t = np.linspace(0, 2 * np.pi, 1000)  # Parameter from 0 to 2*pi

# Define the parametric equations for the trefoil knot
x = np.sin(t) + 2 * np.sin(2 * t)
y = np.cos(t) - 2 * np.cos(2 * t)
#z = -np.sin(3 * t)

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the trefoil knot
#ax.plot(x, y, z, lw=2)
ax.plot(x, y, lw=2)

# Customize the plot (optional)
ax.set_title("Trefoil Knot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")

plt.show()
