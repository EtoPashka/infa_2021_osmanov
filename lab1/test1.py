import numpy as np
import matplotlib.pyplot as plt

a = int(input())

if a == 1:
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, x**2)
    plt.show()
elif a == 2:
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
    plt.show()
elif a == 3:
    x = np.arange(-10, 10.01, 0.01)
    plt.plot(x, np.sin(x), x, np.cos(x), x, -x)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$f(x)$')
    plt.title(r'$f_1(x)=\sin(x),\ f_2(x)=\cos(x),\ f_3(x)=-x$')
    plt.grid(True)
    plt.show()
elif a == 4:
    x = np.arange(-10, 10.01, 0.01)
    plt.figure(figsize=(10, 5))
    plt.plot(x, np.sin(x), label=r'$f_1(x)=\sin(x)$')
    plt.plot(x, np.cos(x), label=r'$f_2(x)=\cos(x)$')
    plt.plot(x, -x, label=r'$f_3(x)=-x$')
    plt.xlabel(r'$x$', fontsize=14)
    plt.ylabel(r'$f(x)$', fontsize=14)
    plt.grid(True)
    plt.legend(loc='best', fontsize=12)
    plt.savefig('figure_with_legend.png')
    plt.show()
else:
    pass