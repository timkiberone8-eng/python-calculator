# Урок 9, шаг 10 (слайды 19-20). Визуализация 3: выручка за каждый день.
#
# Запуск из папки session6:
#     python 10_chart_daily_revenue.py
#
# Окно с графиком держит программу, пока его не закроешь.
#
# Чем отличается от слайда:
# - пароль postgres вместо 1111.
# - на слайде график строится из daily_revenue_data, но откуда она
#   взялась, на слайдах не показано: это задание 3, которое делают
#   самостоятельно. Здесь запрос из 07_revenue_by_day.py повторён в начале.

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

# Запрос из задания 3
cursor.execute("""
SELECT sale_date, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY sale_date
ORDER BY sale_date
""")
daily_revenue_data = cursor.fetchall()

cursor.close()
connection.close()

# Подготовка данных для визуализации
dates = [row[0] for row in daily_revenue_data]     # Даты продаж
revenues = [row[1] for row in daily_revenue_data]  # Выручка за каждый день

# Построение линейного графика
plt.figure(figsize=(10, 6))
plt.plot(dates, revenues, marker='o', color='blue')
plt.title("Ежедневная выручка")
plt.xlabel("Дата")
plt.ylabel("Выручка")
plt.xticks(rotation=45)  # Поворот дат на оси X для удобства чтения
plt.tight_layout()       # Подгонка графика под размер окна
plt.show()
