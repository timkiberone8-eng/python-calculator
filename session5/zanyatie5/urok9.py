# Занятие 5 (04.10): Python + база данных.
#
# Перед первым запуском, один раз, в терминале VS Code:
#     pip install psycopg2-binary
#
# Запуск: python urok9.py
# Программа сама создаёт таблицу sales в базе kiber, кладёт туда продажи
# и спрашивает у базы два итога. Запускать можно сколько угодно раз:
# таблица каждый раз создаётся заново.

import psycopg2

PASSWORD = "postgres"

connection = psycopg2.connect(
    dbname="kiber",
    user="postgres",
    password=PASSWORD,
    host="127.0.0.1",
    port="5432",
)
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS sales")
cursor.execute("""
    CREATE TABLE sales (
        id SERIAL PRIMARY KEY,
        product TEXT,
        quantity INTEGER,
        price NUMERIC(8,2),
        sale_date DATE
    )
""")

sales = [
    ("Laptop", 10, 700, "2026-10-01"),
    ("Smartphone", 25, 300, "2026-10-01"),
    ("Tablet", 15, 250, "2026-10-02"),
    ("Headphones", 50, 50, "2026-10-02"),
    ("Smartwatch", 30, 150, "2026-10-03"),
]

for sale in sales:
    cursor.execute(
        "INSERT INTO sales (product, quantity, price, sale_date) VALUES (%s, %s, %s, %s)",
        sale,
    )

connection.commit()
print("Продажи записаны в базу")

print("\nВыручка по товарам:")
cursor.execute("""
    SELECT product, SUM(quantity * price) AS revenue
    FROM sales
    GROUP BY product
    ORDER BY revenue DESC
""")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

print("\nПродано штук по дням:")
cursor.execute("""
    SELECT sale_date, SUM(quantity)
    FROM sales
    GROUP BY sale_date
    ORDER BY sale_date
""")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

cursor.close()
connection.close()
