# Запас 2, срез по базам данных (урок 10), часть 4 (слайд 7): две диаграммы.
#
# Нужны таблицы с данными: extra2_1_tables.py, потом extra2_2_data.py.
#
# Запуск из папки session6:
#     python extra2_4_charts.py
#
# Сначала откроется первая диаграмма. Вторая появится, только когда
# закроешь окно первой: plt.show() ждёт закрытия окна.

import psycopg2
import matplotlib.pyplot as plt

connection = psycopg2.connect(
    dbname="company_data",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)
cursor = connection.cursor()

# Запрос 1 из extra2_3_analysis.py: сумма продаж по сотрудникам
cursor.execute("""
SELECT employees.name, SUM(sales.sale_amount) AS total_sales
FROM employees
JOIN sales ON sales.employee_id = employees.id
GROUP BY employees.name
ORDER BY total_sales DESC, employees.name
""")
by_employee = cursor.fetchall()

# Запрос 2 из extra2_3_analysis.py: средняя сумма продажи по продуктам
cursor.execute("""
SELECT product_name, ROUND(AVG(sale_amount), 2) AS avg_amount
FROM sales
GROUP BY product_name
ORDER BY product_name
""")
by_product = cursor.fetchall()

cursor.close()
connection.close()

# 1. Столбчатая: по оси X имена, по оси Y сумма продаж
names = [row[0] for row in by_employee]
totals = [row[1] for row in by_employee]

plt.figure(figsize=(10, 6))
plt.bar(names, totals, color='blue', alpha=0.7)
plt.title("Общая сумма продаж по сотрудникам")
plt.xlabel("Сотрудник")
plt.ylabel("Сумма продаж")
plt.show()

# 2. Круговая: средняя сумма продажи по продуктам
products = [row[0] for row in by_product]

# float(...): средние база отдаёт точным числом Decimal, а круговая
# диаграмма в matplotlib 3.11 его не принимает (TypeError: ufunc
# 'isfinite' not supported...). Переводим в обычное число с точкой.
averages = [float(row[1]) for row in by_product]

plt.figure(figsize=(8, 8))
plt.pie(averages, labels=products, autopct='%1.1f%%')
plt.title("Средняя сумма продажи по продуктам")
plt.show()
