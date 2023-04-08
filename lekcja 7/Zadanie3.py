import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("imiona.xlsx")
df1 = df[df['Rok'] >= 2013]
x = df["Plec"].unique()
y = df1.groupby(["Plec"])["Plec"].count()
plt.pie(y, autopct="%.2f%%")
plt.show()
