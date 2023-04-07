import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("imiona.xlsx")
df1 = df.groupby(["Rok"])["Rok"].count()
x = df['Rok'].unique()
print(x)
df1.plot(x=x)
plt.show()
