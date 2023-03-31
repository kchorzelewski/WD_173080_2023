import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=';')

for x in df["Sprzedawca"].unique():
    print(x)
