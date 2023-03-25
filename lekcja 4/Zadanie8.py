import numpy as np

def func(t, kierunek=1):
    y, x = np.shape(t)
    if kierunek:
        if not x%2:
            return 0
        t = np.array_split(t, x/2)
    else:
        if not y%2:
            return 0
        t = np.array_split(t, y/2, 1)
    print(t)

func(np.arange(20).reshape((5,4)),0)
