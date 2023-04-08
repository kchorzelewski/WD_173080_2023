import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("imiona.xlsx")
y = df.groupby(["Plec"])["Plec"].count()
x = df["Plec"].unique()
plt.bar(x, y)
plt.show()
