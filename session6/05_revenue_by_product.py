# Урок 9, шаг 5 (слайд 11). Задание 1: общая выручка по каждому продукту.
#
# Запуск из папки session6:
#     python 05_revenue_by_product.py
#
# Выручка одной продажи = количество * цена. У каждого продукта
# складываем выручку всех его продаж.
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

# GROUP BY product_name: собрать строки с одинаковым продуктом в одну группу.
# SUM(...): сложить внутри каждой группы.
# AS total_revenue: дать столбцу-итогу имя, чтобы сослаться на него в ORDER BY.
cursor.execute("""
SELECT product_name, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC
""")

# fetchall(): забрать ответ базы целиком, списком строк.
# Каждая строка: row[0] продукт, row[1] выручка.
revenue_data = cursor.fetchall()
for row in revenue_data:
    print(f"Продукт: {row[0]}, Общая выручка: {row[1]}")

cursor.close()
connection.close()
