import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4, 5]
y = [0.99, 0.49, 0.35, 0.253, 0.18]
plt.errorbar(x, y, xerr=0.05, yerr=0.1)
plt.grid()

p, v = np.polyfit(x, y, deg = 3, cov = True)

p_f = np.poly1d(p)

k = np.arange(0., 5., 0.01)

plt.plot(k, p_f(k))




plt.show()

