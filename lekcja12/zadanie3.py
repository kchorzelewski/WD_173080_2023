import pandas as pd
import numpy as np
import matplotlib as plt
import seaborn as sns

fig, (ax1, ax2) = plt.subplots(ncols=2)
fig.suptitle("liczba narodzin w pandasie")
fig.subtitle("liczba narodzina w seaborn")



df = pd.read_excel('imiona.xlsx')
data = df[(df["Rok"] >= 2010) & (df["Rok"] <= 2015)]
data_grouped = data.groupby("Plec")["Liczba"].sum()
data_grouped.plot.bar()
sns.barplot(data=data, x="Plec", y="Liczba", estimator=sum, ax=ax2)

plt.show()



