import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def rzut(n):
    w = []
    for i in range(n):
        d6 = np.random.randint(1,7) + np.random.randint(1,7)
        w.append(d6)
    plt.hist(w, bins=range(2, 13))
    plt.show()
rzut(300)
