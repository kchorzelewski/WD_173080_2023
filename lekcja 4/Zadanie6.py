import numpy as np

a = "malina"
b = "lizak"
c = "jagoda"
a1 = np.array(list(a))
b1 = np.array(list(b))
c1 = np.array(list(c))
mat = np.zeros((6,6),dtype=str)
mat[:,0] = a1
mat[2,:-1] = b1
mat[5,:] = c1
print(mat)
