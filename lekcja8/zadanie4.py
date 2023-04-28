import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,30,0.1)
y = np.arange(1.5,31.5,0.1)
plt.plot(np.sin(x)+2)
plt.plot(np.cos(y))
plt.xticks()
plt.xlabel(np.arange(10))
plt.show()
