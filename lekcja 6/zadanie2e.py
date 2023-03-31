import pandas as pd

df = pd.read_excel("imiona.xlsx")

print(df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]['Rok'].count())
