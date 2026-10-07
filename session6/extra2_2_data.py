# Дополнительно 2, срез по базам данных (урок 10), часть 2 (слайды 4-5):
# заполнить таблицы employees и sales данными со слайдов.
#
# Нужна база с таблицами из extra2_1_tables.py.
#
# Запуск из папки session6:
#     python extra2_2_data.py

import psycopg2

connection = psycopg2.connect(
    dbname="company_data",
    user="postgres",
    password="postgres",
    host="127.0.0.1",
    port="5432"
)
cursor = connection.cursor()

# Очистить обе таблицы и начать нумерацию id заново с 1, чтобы второй
# запуск этого файла не задвоил данные. TRUNCATE: удалить все строки,
# RESTART IDENTITY: сбросить счётчик SERIAL. Обычный DELETE счётчик
# не сбрасывает: сотрудники получили бы номера 6-10, а продажи ниже
# ссылаются на 1-5, и база отказала бы (внешний ключ).
cursor.execute("TRUNCATE sales, employees RESTART IDENTITY")

# Сотрудники: имя, должность, дата найма. id база поставит сама: 1, 2, 3...
employees = [
    ("Anna Ivanova", "Manager", "2023-06-15"),
    ("Boris Petrov", "Sales Rep", "2024-01-10"),
    ("Maria Sidorova", "Sales Rep", "2024-02-05"),
    ("Ivan Smirnov", "Sales Rep", "2024-03-01"),
    ("Olga Volkova", "Manager", "2023-09-12"),
]
for employee in employees:
    cursor.execute("INSERT INTO employees (name, position, hire_date) VALUES (%s, %s, %s)", employee)

# Продажи: номер сотрудника, продукт, сколько штук, сумма, дата.
# Дату можно передать текстом '2024-02-15': база сама превратит её в DATE.
sales = [
    (1, "Laptop", 5, 1000, "2024-02-15"),
    (2, "Tablet", 10, 250, "2024-02-16"),
    (3, "Smartphone", 2, 500, "2024-02-17"),
    (4, "Smartwatch", 6, 150, "2024-03-15"),
    (5, "Laptop", 8, 1000, "2024-03-16"),
]
for sale in sales:
    cursor.execute("INSERT INTO sales (employee_id, product_name, quantity, sale_amount, sale_date) VALUES (%s, %s, %s, %s, %s)", sale)

connection.commit()
print("Сотрудников записано:", len(employees))
print("Продаж записано:", len(sales))

cursor.close()
connection.close()
