import numpy as np
import matplotlib.pyplot as plt

with plt.xkcd():
    x = np.arange(-10, 10.01, 0.01)
    print('y =', end=' ')
    y = eval(input())
    plt.plot(x, y)
    plt.grid(True)
    plt.show()