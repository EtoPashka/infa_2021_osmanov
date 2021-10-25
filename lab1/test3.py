import numpy as np
import matplotlib.pyplot as plt
plt.subplot(111, polar=True)
phi = np.arange(0, 2*np.pi, 0.01)
rho = 2*phi
plt.plot(phi, rho, lw=2)
plt.show()