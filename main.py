import matplotlib.pyplot as plt
import random

plt.style.use("seaborn-whitegrid")

direction_choices = [
    (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

walks = 5
steps = 500

for walk_num in range(walks):
    x_coor = y_coor = steps

    path_x = [x_coor]
    path_y = [y_coor]
    for _ in range(steps):
        direction = random.choice(direction_choices)
        x_coor += direction[0]
        y_coor += direction[1]

        path_x.append(x_coor)
        path_y.append(y_coor)

    plt.plot(path_x, path_y, label=str(walk_num + 1))  # Plot some data on the axes.
    plt.title("Random walk")
    plt.xlabel("x coordinate")
    plt.ylabel("y coordinate")
plt.legend()
plt.show()
