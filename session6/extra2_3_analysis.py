# Запас 2, срез по базам данных (урок 10), часть 3 (слайд 6): анализ.
#
# Нужны таблицы с данными: extra2_1_tables.py, потом extra2_2_data.py.
#
# Запуск из папки session6:
#     python extra2_3_analysis.py

import psycopg2

connection = psycopg2.connect(
    dbname="company_data",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)
cursor = connection.cursor()

# 1. Общая сумма продаж по сотрудникам.
# Имя лежит в employees, суммы в sales. JOIN склеивает строки двух таблиц:
# к каждой продаже приставляется строка того сотрудника, чей id совпал
# с employee_id продажи (условие после ON).
# Имена столбцов пишем с именем таблицы через точку (employees.name),
# потому что id и в обеих таблицах свой.
# Второй ключ в ORDER BY (employees.name) нужен для равных сумм:
# без него база ставит их в каком угодно порядке.
print("1. Общая сумма продаж по сотрудникам")
cursor.execute("""
SELECT employees.name, SUM(sales.sale_amount) AS total_sales
FROM employees
JOIN sales ON sales.employee_id = employees.id
GROUP BY employees.name
ORDER BY total_sales DESC, employees.name
""")
for row in cursor.fetchall():
    print(f"{row[0]} - {row[1]}")

# 2. Средняя сумма продажи для каждого продукта.
# AVG: среднее. ROUND(..., 2): округлить до двух знаков после точки,
# иначе PostgreSQL выдаёт среднее с длинным хвостом нулей.
print()
print("2. Средняя сумма продажи по продуктам")
cursor.execute("""
SELECT product_name, ROUND(AVG(sale_amount), 2) AS avg_amount
FROM sales
GROUP BY product_name
ORDER BY product_name
""")
for row in cursor.fetchall():
    print(f"{row[0]} - {row[1]}")

# 3. Количество продаж по месяцам.
# TO_CHAR(sale_date, 'YYYY-MM'): дата в виде текста «год-месяц»,
# например 2024-02. По нему и группируем.
# COUNT(*): сколько строк в группе, то есть сколько продаж.
print()
print("3. Количество продаж по месяцам")
cursor.execute("""
SELECT TO_CHAR(sale_date, 'YYYY-MM') AS month, COUNT(*) AS sales_count
FROM sales
GROUP BY month
ORDER BY month
""")
for row in cursor.fetchall():
    print(f"{row[0]} - {row[1]}")

cursor.close()
connection.close()
