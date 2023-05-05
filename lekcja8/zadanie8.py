import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('zamowienia.csv', delimiter=";")
y = df.groupby(['Sprzedawca'])['Sprzedawca'].count()
x = y.keys()

plt.pie(y, labels=x, autopct=lambda pct: "{:.1f}%".format(pct))
plt.show()
