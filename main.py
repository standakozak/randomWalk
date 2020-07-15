import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

#plt.style.use("seaborn-whitegrid")
plt.xkcd()

# Possible directions for step
direction_choices = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

steps = 1000
x_coor = y_coor = steps
x_path = [x_coor]
y_path = [y_coor]

# Plot init
fig, ax = plt.subplots()
ax.plot(x_path, y_path, "kx")  # Start marker
path_line, = ax.plot(x_path,y_path,"r-",linewidth=3)
position_dot, = ax.plot(x_path, y_path, "bo", linewidth=3)


for _ in range(steps):  #Setting the path
    direction = random.choice(direction_choices)
    x_coor += direction[0]
    y_coor += direction[1]

    x_path.append(x_coor)
    y_path.append(y_coor)
ax.set_ylim(min(y_path) - 1, max(y_path) + 1)
ax.set_xlim(min(x_path) - 1, max(x_path) + 1)

animations = []


def update_line(num, position, _line, dot):
    """
    Animation of the path
    """
    _line.set_data(position[0][:num + 1],position[1][:num + 1])
    dot.set_data(position[0][num], position[1][num])

    return _line, dot


animations.append(animation.FuncAnimation(fig,update_line,steps,fargs=((x_path, y_path), path_line, position_dot),
                                          interval=200,blit=True, repeat_delay=400))


plt.show()
