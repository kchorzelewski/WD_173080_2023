import pandas as pd

df = pd.read_excel("imiona.xlsx")

print(df.groupby(['Plec'])['Plec'].count())
