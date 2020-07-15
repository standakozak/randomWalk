import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

steps = 25

# Plot init

plt.xkcd()
fig, ax = plt.subplots()
plt.title("RANDOM WALK")

# Possible directions for step
direction_choices = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

animations = []
lines = dots = []


def update_path(num, position,  _line, _dot):
    """
    Animation of the path
    """

    _line.set_data(position[0][:num + 1], position[1][:num + 1])
    _dot.set_data(position[0][num], position[1][num])
    return _line, _dot


ax.plot(steps, steps, "kx")  # Start marker
x_coor = y_coor = steps
x_path = [x_coor]
y_path = [y_coor]

path_line, = ax.plot(x_path, y_path, "r-", linewidth=3)

position_dot, = ax.plot(x_path, y_path, "bo", linewidth=3)

for _ in range(steps):  #Setting the path
    direction = random.choice(direction_choices)
    x_coor += direction[0]
    y_coor += direction[1]

    x_path.append(x_coor)
    y_path.append(y_coor)

ax.set_xlim(min(x_path) - 1, max(x_path) + 1)
ax.set_ylim(min(y_path) - 1, max(y_path) + 1)
path_ani = animation.FuncAnimation(fig, update_path, steps,
                                   fargs=((x_path, y_path), path_line, position_dot),
                                   interval=300, repeat=True, blit=True, repeat_delay=400)
animations.append(path_ani)

plt.show()
