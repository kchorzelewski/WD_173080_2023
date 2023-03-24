import numpy as np

def func(n):
    x = np.arange(1, n*n+1).reshape(n,n)
    print(x)
    print(x.shape)

func(4)
