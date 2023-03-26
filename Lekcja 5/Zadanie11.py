import numpy as np

x = np.arange(12)
x = x.reshape(3,4)

y = np.arange(12)
y = y.reshape(4,3)

z = np.arange(12)
z = z.reshape(2,6)

x = x.ravel()
y = y.ravel()
z = z.ravel()
print(x)
print(y)
print(z)
print("każde z nich wyglądają identycznie")
