import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_excel('imiona.xlsx')

figure, axis = plt.subplots(1,3)
data = df.groupby(["Plec"])["Plec"].count()

x = ["K", "M"]
c = ['red', 'green']
axis[0].bar(x, data, color=c)
axis[0].set_title("wykres 1")


x = df["Rok"].unique()
m = df[df["Plec"] == "M"].groupby(["Rok"])["Rok"].count()
k = df[df["Plec"] == "K"].groupby(["Rok"])["Rok"].count()
new = []
for i in range(len(m)):
    new.append([m[2000+i], k[2000+i]])
axis[1].plot(x, new)
axis[1].set_title("wykres 2")


data = df.groupby(["Rok"])["Rok"].sum()
axis[2].bar(x, data)
axis[2].set_title("wykres 3")

plt.show()


