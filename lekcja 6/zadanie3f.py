import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=';')
df1 = df[df['Data zamowienia'].str[:4] == "2004"]
print(df1['Utarg'].mean())
