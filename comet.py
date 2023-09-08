import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define the comet's initial position and velocity
x0, y0 = 0, 0
vx, vy = 0.1, 0.1  # Adjust the velocity as desired

# Create a function to update the comet's position in each frame
def update_comet(num, line):
    global x0, y0, vx, vy
    
    # Update the comet's position
    x0 += vx
    y0 += vy
    
    # Update the line data (comet's path)
    line.set_data(x0, y0)
    
    return line,

# Create a figure and axis for the animation
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)  # Adjust the x-axis limits as needed
ax.set_ylim(-1, 1)  # Adjust the y-axis limits as needed

# Create a line to represent the comet's path
line, = ax.plot([], [], 'b.', markersize=10)

# Create an animation
ani = animation.FuncAnimation(fig, update_comet, frames=200, fargs=(line,),
                              interval=50, blit=True)

plt.title('Comet Animation')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# To display the animation in a Jupyter Notebook, use the following line:
# from IPython.display import HTML
# HTML(ani.to_jshtml())

# To save the animation as a GIF, use the following line:
ani.save('comet_animation.gif', writer='pillow', fps=20)

# To display the animation in a standalone window (not recommended for some IDEs):
plt.show()
