import numpy as np

def func(n, m):
    x = np.logspace(n-1, m, num=m, base=n)
    print(x)
func(2,4)
