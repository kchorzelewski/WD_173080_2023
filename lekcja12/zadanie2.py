import pandas as pd
import numpy as np

df = pd.read_excel("imiona.xlsx")
dfM = df[df["Plec"] == "M"]
dfK = df[df["Plec"] == "K"]

results = df.groupby(["Imie", "Plec"])["Liczba"].sum().reset_index()
k = results[results['Plec'] == "K"].reset_index()
k = k["Liczba"].idxmax()
print(k)



