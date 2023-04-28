import matplotlib.pyplot as plt
import numpy as np

plt.plot(1/np.arange(20))
plt.ylabel("f(x)")
plt.xlabel('x')
plt.axis([0,20,0,1])
plt.show()
