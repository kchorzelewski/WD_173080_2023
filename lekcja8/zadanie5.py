import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris.data', delimiter=',', header=None)


x = df[0]
y = df[1]
c = np.random.randint(0, 50, len(df[0]))
s = np.zeros(len(df[0]))

for i in range(len(s)):
    s[i] = np.abs(x[i] - y[i])*5

plt.scatter(x, y, c=c, s=s)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()
