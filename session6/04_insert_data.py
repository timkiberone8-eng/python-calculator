# Урок 9, шаг 4 (слайд 10): записать в таблицу sales пять продаж.
#
# Запуск из папки session6:
#     python 04_insert_data.py
#
# Чем отличается от слайда:
# - пароль postgres вместо 1111.
# - перед записью DELETE FROM sales. На слайде его нет, там вся программа
#   одним файлом и каждый запуск создаёт базу заново. Здесь шаги
#   отдельными файлами, и без DELETE второй запуск этого шага записал бы
#   те же продажи ещё раз: выручка во всех итогах стала бы вдвое больше.
# - на слайде внутри скобок видны серые подсказки PyCharm: year:, month:,
#   day:, query:. Это не код, их не набирают. С ними Python
#   падает с SyntaxError.

import psycopg2
from datetime import datetime

connection = psycopg2.connect(
    database="sales_data",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)
cursor = connection.cursor()

# Убираем продажи прошлого запуска, если они есть.
# DELETE без WHERE удаляет все строки, сама таблица остаётся.
cursor.execute("DELETE FROM sales")

# Добавляем данные в таблицу "sales".
# sales_data здесь просто список Python, так он назван на слайде.
# Каждая продажа: товар, сколько штук, цена за штуку, дата.
sales_data = [
    ("Laptop", 10, 700, datetime(2024, 1, 10)),
    ("Smartphone", 25, 300, datetime(2024, 1, 11)),
    ("Tablet", 15, 250, datetime(2024, 1, 12)),
    ("Headphones", 50, 50, datetime(2024, 1, 13)),
    ("Smartwatch", 30, 150, datetime(2024, 1, 14)),
]

# %s: место для значения. psycopg2 сам подставит туда значения из sale
# по порядку и сам расставит кавычки, где они нужны.
for sale in sales_data:
    cursor.execute("INSERT INTO sales (product_name, quantity, price, sale_date) VALUES (%s, %s, %s, %s)", sale)

connection.commit()
print("Данные добавлены")

cursor.close()
connection.close()
