import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("imiona.xlsx")
df1 = df.groupby(["Plec"])["Plec"].count()
print(df1)
df1.plot()
plt.show()
