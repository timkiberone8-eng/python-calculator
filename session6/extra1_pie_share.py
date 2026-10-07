# Дополнительно 1, домашнее задание урока 9 (слайд 21), пункт 1:
# круговая диаграмма, какую долю общей выручки дал каждый продукт.
#
# Нужны таблица sales с продажами (шаги 2-4) и matplotlib.
#
# Запуск из папки session6:
#     python extra1_pie_share.py

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

# Тот же запрос, что в задании 1: выручка по продуктам
cursor.execute("""
SELECT product_name, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC
""")
revenue_data = cursor.fetchall()

cursor.close()
connection.close()

products = [row[0] for row in revenue_data]

# float(...): деньги база отдаёт точным числом Decimal. Столбики и линии
# его принимают, а круговая диаграмма в matplotlib 3.11 нет: падает
# с TypeError: ufunc 'isfinite' not supported for the input types...
# Поэтому переводим в обычное число с точкой, float.
revenue = [float(row[1]) for row in revenue_data]

# Доли посчитаем и сами, чтобы сверить с диаграммой.
# :.1f значит «один знак после точки».
total = sum(revenue)
print(f"Общая выручка: {total}")
for row in revenue_data:
    share = float(row[1]) / total * 100
    print(f"{row[0]}: {share:.1f}%")

# plt.pie рисует круг, сумма всех кусков = 100 %.
# autopct='%1.1f%%': подписать на каждом куске его долю в процентах
# с одним знаком после точки (%% в конце печатает сам знак %).
plt.figure(figsize=(8, 8))
plt.pie(revenue, labels=products, autopct='%1.1f%%')
plt.title("Доля каждого продукта в общей выручке")
plt.show()
