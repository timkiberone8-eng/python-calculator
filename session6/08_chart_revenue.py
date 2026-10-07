# Урок 9, шаг 8 (слайды 14-16). Визуализация 1: выручка по продуктам
# столбиками.
#
# Нужна библиотека matplotlib. Если не ставил вместе с psycopg2:
#     python -m pip install matplotlib
#
# Запуск из папки session6:
#     python 08_chart_revenue.py
#
# plt.show() открывает окно с графиком, и программа ждёт, пока ты его
# не закроешь. Пока окно открыто, терминал занят. Закрыл окно крестиком,
# программа закончилась.
#
# Чем отличается от слайда:
# - пароль postgres вместо 1111.
# - на слайде график рисуется в конце той же программы, где задание 1.
#   Здесь отдельный файл, поэтому запрос из задания 1 повторён в начале.
# - на слайде график назван гистограммой. Правильнее «столбчатая
#   диаграмма»: гистограммой называют другой график.

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

# Запрос из задания 1
cursor.execute("""
SELECT product_name, SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC
""")
revenue_data = cursor.fetchall()

# Данные уже у нас, подключение больше не нужно
cursor.close()
connection.close()

# Данные для диаграммы: два списка, подписи и высоты столбиков
products = [row[0] for row in revenue_data]
revenue = [row[1] for row in revenue_data]

# figsize=(10, 6): размер окна, ширина и высота
# alpha=0.7: прозрачность, 1 непрозрачно, 0 совсем не видно
plt.figure(figsize=(10, 6))
plt.bar(products, revenue, color='blue', alpha=0.7)
plt.title("Общая выручка по продуктам")
plt.xlabel("Продукт")
plt.ylabel("Выручка")
plt.show()
