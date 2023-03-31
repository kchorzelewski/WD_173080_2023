import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=';')

df1 = df.sort_values(by=['Utarg'], ascending=False)
print(df1.head(5))
