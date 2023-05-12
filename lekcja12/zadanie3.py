import pandas as pd
import numpy as np
import matplotlib as plt

df = pd.read_excel('imiona.xlsx')
data = df[(df["Rok"] >= 2010) & (df["Rok"] <= 2015)]
data_grouped = data.groupby("Plec")["Liczba"].sum()
data_grouped.plot.bar()

plt.show()



