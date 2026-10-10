# Урок 4, мини-проект «Моя библиотека».
#
# Запускать из папки urok4:
#     python my_library.py
#
# Первая программа курса, которая ПОМНИТ данные между запусками.
# Всё, что было до неё, забывало всё при выходе.
#
# Здесь собрано вместе то, что прошли за три занятия: функции (урок 1),
# разнесение по функциям (урок 2), try/except (урок 3) и файлы (урок 4).

import csv

# Имя файла в одном месте, а не в трёх. Здесь оно СВОЁ, не books.csv:
# в books.csv из прошлого шага первой строкой лежит заголовок
# «Название, Автор, Год», и эта программа показала бы его как книгу №1.
# Хороший вопрос группе: почему так вышло и как это чинят (пропуском
# первой строки через next(reader), как в books_csv.py).
FILENAME = "my_books.csv"


def add_book(title, author, year):
    """Дописывает одну книгу в конец файла."""
    # Режим "a" — дописать. Если поставить "w", каждая новая книга
    # затирала бы все предыдущие.
    with open(FILENAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])


def show_books():
    """Печатает все книги из файла."""
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            books = list(reader)
    except FileNotFoundError:
        # Файла ещё нет — это не поломка, а нормальный первый запуск.
        # Без этого except программа падала бы у каждого, кто запустил
        # её впервые и сразу выбрал пункт 2.
        print("Файл не найден. Пока что нет книг.")
        return

    if not books:
        print("Книг пока нет.")
        return

    print("Ваши книги:")
    # enumerate(books, 1) выдаёт пары (номер, книга), нумерация с единицы
    for i, book in enumerate(books, 1):
        title, author, year = book
        print(f"{i}. {title} — {author}, {year}")


def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Выход")
        choice = input("Выбери пункт: ").strip()

        if choice == "1":
            title = input("Название: ")
            author = input("Автор: ")
            year = input("Год: ")
            add_book(title, author, year)
            print("Книга добавлена.")
        elif choice == "2":
            show_books()
        elif choice == "3":
            print("До свидания!")
            break       # единственный выход из while True
        else:
            # Ветка else обязательна: без неё опечатка в пункте меню
            # выглядит как «программа зависла», хотя она просто молчит.
            print("Нет такого пункта. Введи 1, 2 или 3.")


if __name__ == "__main__":
    main()
