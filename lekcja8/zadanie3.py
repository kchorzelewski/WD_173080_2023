import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,30,0.1)
plt.title("Wykres sin(x), cos(x)")
plt.plot(np.sin(x), label="sin(x)")
plt.plot(np.cos(x), label="cos(x)")
plt.xlabel("x")
plt.ylabel("sin(x), cos(x)")
plt.legend(loc="upper right")
plt.show()
