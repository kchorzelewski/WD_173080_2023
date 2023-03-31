import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=';')

print(df.groupby(["Kraj"])["Kraj"].count())
