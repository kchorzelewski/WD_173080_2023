import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("zamowienia.csv", delimiter=";")
y = df.groupby(["Sprzedawca"])["Sprzedawca"].count()
x = df["Sprzedawca"].unique()
plt.bar(x,y)
plt.show()
