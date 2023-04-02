import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=';')
df1 = df[df['Data zamowienia'].str[:4] == "2004"]
df1.to_csv('zamowienia_2004.csv')
df1 = df[df['Data zamowienia'].str[:4] == "2005"]
df1.to_csv('zamowienia_2005.csv')
