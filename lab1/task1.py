import numpy as np

for x in [1, 10, 1000]:
    y = np.log(np.exp(1/(np.sin(x)+1))/(5/4+x**(-15)))/np.log(1+x**2)
    print(y)