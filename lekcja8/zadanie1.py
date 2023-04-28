import matplotlib.pyplot as plt
import numpy as np

plt.plot(1/np.arange(21), label="f(x) = 1/x")
plt.ylabel("f(x)")
plt.xlabel('x')
plt.legend()
plt.axis([0,20,0,1])
plt.show()
