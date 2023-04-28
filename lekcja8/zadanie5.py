import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# df = pd.read_csv("iris.data", header=None)
# print(df)

data ={'a':np.arange(50),# 1, 2, 3, ..., 48, 49
       'c':np.random.randint(0,50,50),
       'd':np.random.randn(50)}
data['b']=data['a']+10*np.random.randn(50) # dodanie nowego klucza ‘b’
data['d']=np.abs(data['d'])*100 # nadpisanie wartości klucza ‘d’

plt.scatter('a','b',c='c',s='d',data=data)
plt.xlabel('wartość a')
plt.ylabel('wartość b')
plt.show()
# x = np.arange(0,30,0.1)
# plt.title("Wykres sin(x), cos(x)")
# plt.plot(np.cos(x), label="cos(x)")
# plt.xlabel("x")
# plt.ylabel("sin(x), cos(x)")
