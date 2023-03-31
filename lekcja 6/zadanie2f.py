import pandas as pd

df = pd.read_excel("imiona.xlsx")

print("chłopcy:",df[(df['Plec'] == 'M')]['Plec'].count())
print("dziewczynki:",df[(df['Plec'] == 'K')]['Plec'].count())
