# Дополнительно 1, домашнее задание урока 9 (слайд 21), пункт 2:
# дни с наибольшим объёмом продаж, столбчатой диаграммой.
#
# Объём здесь считаем в штуках: SUM(quantity). Если считать в деньгах,
# замени SUM(quantity) на SUM(quantity * price): тогда первые три дня
# будут другие.
#
# Нужны таблица sales с продажами (шаги 2-4) и matplotlib.
#
# Запуск из папки session6:
#     python extra1_top_days.py

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

# ORDER BY ... DESC: сверху дни, в которые продали больше всего.
# LIMIT 3: из ответа взять только первые три строки.
# Сколько дней показать, решаешь сам: поменяй 3.
cursor.execute("""
SELECT sale_date, SUM(quantity) AS total_quantity
FROM sales
GROUP BY sale_date
ORDER BY total_quantity DESC
LIMIT 3
""")
top_days = cursor.fetchall()

cursor.close()
connection.close()

for row in top_days:
    print(f"Дата: {row[0]}, Продано: {row[1]}")

# str(row[0]) превращает дату в текст вроде 2024-01-13. Иначе matplotlib
# расставит столбики по календарю, а не по местам: первое место
# окажется не первым слева.
days = [str(row[0]) for row in top_days]
quantities = [row[1] for row in top_days]

plt.figure(figsize=(8, 6))
plt.bar(days, quantities, color='orange')
plt.title("Дни с наибольшим количеством проданных товаров")
plt.xlabel("Дата")
plt.ylabel("Продано, штук")
plt.show()
