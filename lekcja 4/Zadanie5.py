import numpy as np

def func(n):
    wektor = np.arange(1,n+1)
    wektor = wektor[::-1]
    diag = np.diag(wektor)
    print(diag)

func(5)
