# Урок 9, шаг 9 (слайды 17-18). Визуализация 2: сколько товаров
# продано по дням, линией с точками.
#
# Запуск из папки session6:
#     python 09_chart_quantity.py
#
# Окно с графиком держит программу, пока его не закроешь.
#
# Чем отличается от слайда:
# - пароль postgres вместо 1111.
# - запрос из задания 2 повторён в начале, потому что файл отдельный.
# - на слайде в plt.plot( видна серая подсказка PyCharm *args:.
#   Это не код, её не набирают.

import psycopg2
import matplotlib.pyplot as plt

connection = psycopg2.connect(
    database="sales_data",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)
cursor = connection.cursor()

# Запрос из задания 2
cursor.execute("""
SELECT sale_date, SUM(quantity) AS total_quantity
FROM sales
GROUP BY sale_date
ORDER BY sale_date
""")
daily_sales_data = cursor.fetchall()

cursor.close()
connection.close()

# Данные для графика
dates = [row[0] for row in daily_sales_data]
quantities = [row[1] for row in daily_sales_data]

# marker='o': кружок в каждой точке
# xticks(rotation=45): повернуть подписи дат, чтобы не наезжали друг на друга
# Под осью будут подписи вроде 01-10 00 и 01-10 12: месяц-день и час.
# matplotlib ставит деления каждые 12 часов, точки стоят на 00.
plt.figure(figsize=(10, 6))
plt.plot(dates, quantities, marker='o', color='green')
plt.title("Количество проданных товаров по дням")
plt.xlabel("Дата")
plt.ylabel("Количество проданных товаров")
plt.xticks(rotation=45)
# Подписи «Дата» под осью в окне не видно: повёрнутые даты выталкивают
# её за нижний край. На слайде 18 так же. Лечит строка plt.tight_layout()
# перед plt.show(), она есть в шаге 10.
plt.show()
