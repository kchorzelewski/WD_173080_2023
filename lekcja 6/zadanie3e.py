import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=';')

print(df[(df['Data zamowienia'].str[:4] == "2005") & (df['Kraj'] == 'Polska')])

