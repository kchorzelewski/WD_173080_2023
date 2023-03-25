import numpy as np


def func(n):
    scalar = 0
    x = np.diag(np.ones(n)*2)
    for i in range(4,n*2+1,2):
        n-=1
        scalar+=1
        x = x + np.diag(np.ones(n)*i, scalar)
        x = x + np.diag(np.ones(n)*i, scalar*(-1))
    print(x)

func(4)
