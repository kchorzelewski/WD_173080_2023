import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,30,0.1)
y = np.arange(3.2,33.2,0.1)
plt.title("Wykres sin(x), sin(x)")
plt.plot(np.sin(x)+2, label="sin(x)")
plt.plot(np.sin(y), label="sin(x)")
plt.legend()
plt.show()
