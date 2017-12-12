# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.widgets import CheckButtons
from random import random
# from matplotlib import animation
#
#
#
# plt.xlim((-2,2))
# plt.ylim((-2,2))
#
# plt.grid()
#
x = [0]
y = [0]

def generate():
    for i in range(1, 100):
        generate_random_point()

def generate_random_point():
    r = random()
    if (r < .25):
        x.append(x[-1] + 1)
        y.append(y[-1])
    elif (r < .5):
        x.append(x[-1])
        y.append(y[-1] + 1)
    elif (r < .75):
        x.append(x[-1] - 1)
        y.append(y[-1])
    else:
        x.append(x[-1])
        y.append(y[-1] - 1)
#
#
generate()
#
# # plt.plot(x, y, 'ro-', ms=10)
#
# fig = plt.figure()
# ax = plt.axes(xlim=(-2, 2), ylim=(-2, 2))
# line, = ax.plot([], [], lw=2)
#
# # initialization function: plot the background of each frame
# def init():
#     line.set_data([], [])
#     return line,
#
# def animate(i):
#     line.set_data(x[i], y[i])
#     return line,
#
# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#            frames=200, interval=20, blit=True)
#
# plt.show()


import numpy as np
import matplotlib.pyplot as plt

plt.axis([-5, 5, -5, 5])
plt.ion()

plt.grid()
fig, ax = plt.subplots()
ax.set_color_cycle(['red', 'black', 'yellow', 'green', 'blue', 'purple', 'pink', 'gray'])

for i in range(1, len(x)):
    # plt.line(x[i], y[i])
    plt.plot(x[i-1:i+1], y[i-1:i+1])
    plt.scatter(x[i], y[i])

    plt.pause(0.5)

while True:
    plt.pause(0.5)