import numpy as np

x = np.random.randint(10,51,(3,3))
y = np.random.randint(10,51,(4,4))
print(x)
print(y)
for i in range(3):
    print(min(x[i,:]))
    print(min(x[:,i]))
print("-------------")
for i in range(4):
    print(min(y[i,:]))
    print(min(y[:,i]))
    
