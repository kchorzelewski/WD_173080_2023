import pandas as pd
import numpy as np

df = pd.read_excel("imiona.xlsx")

print(df[df["Imie"].str.startswith("B")])


