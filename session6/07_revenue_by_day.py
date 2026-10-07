# Урок 9, шаг 7 (слайд 13). Задание 3: общая выручка за каждый день.
#
# На слайде это задание «попробуйте самостоятельно», кода там нет.
# Сначала попробуй сам по подсказкам слайда: SUM(quantity * price)
# и GROUP BY sale_date. Потом сверься с этим файлом.
#
# Запуск из папки session6:
#     python 07_revenue_by_day.py
#
# Имя daily_revenue_data взято со слайда 19: там график строится
# из переменной с таким именем.

import psycopg2

connection = psycopg2.connect(
    database="sales_data",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)
cursor = connection.cursor()

cursor.execute("""
SELECT sale_date, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY sale_date
ORDER BY sale_date
""")
daily_revenue_data = cursor.fetchall()
for row in daily_revenue_data:
    print(f"Дата: {row[0]}, Выручка: {row[1]}")

cursor.close()
connection.close()
