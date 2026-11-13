import pyarrow.parquet as pq
import pandas as pd
import matplotlib.pyplot as plt

table = pq.read_table("titanic.parquet") #открываем файл и ложим в переменную
df = table.to_pandas() #переводим в таблицу dataframe
df.to_csv("titanic.csv", index=False) #сохраняем таблицу в новый файл
df_csv = pd.read_csv("titanic.csv") #открываем этот созданный файл и загружаем в таблицу
print(df_csv.head())
stats = df_csv.groupby(["Pclass", "Survived"]).size().unstack()
stats.plot(kind="bar", color=["#d9534f", "#5cb85c"])
plt.title("Выживаемость пассажиров в зависимости от класса билета")
plt.xlabel("Класс билета (Pclass)")
plt.ylabel("Количество пассажиров")
plt.legend(["Погибли (0)", "Выжили (1)"], title="Статус")
plt.xticks(rotation=0)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout() #выравниваем отступы по краям окна
plt.show()
