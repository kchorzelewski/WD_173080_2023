import pandas as pd

df = pd.read_excel("imiona.xlsx")

print(df[df['Liczba']>1000])
