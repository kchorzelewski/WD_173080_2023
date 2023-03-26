import numpy as np

x = np.arange(9).reshape(3,3)

e = x.ravel()
for i in e:
    print(i)
