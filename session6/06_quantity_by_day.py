# Урок 9, шаг 6 (слайд 12). Задание 2: сколько товаров продано по дням.
#
# Запуск из папки session6:
#     python 06_quantity_by_day.py
#
# Отличие от слайда: пароль postgres вместо 1111.

import psycopg2

connection = psycopg2.connect(
    database="sales_data",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)
cursor = connection.cursor()

# Группы теперь по дате: все продажи одного дня в одной группе,
# внутри складываем штуки.
cursor.execute("""
SELECT sale_date, SUM(quantity) AS total_quantity
FROM sales
GROUP BY sale_date
ORDER BY sale_date
""")
daily_sales_data = cursor.fetchall()
for row in daily_sales_data:
    print(f"Дата: {row[0]}, Продано: {row[1]}")

cursor.close()
connection.close()
