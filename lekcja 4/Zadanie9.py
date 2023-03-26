import numpy as np

def fibonacci(n):
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

x = np.array([fibonacci(n) for n in range(25)]).reshape((5,5))
