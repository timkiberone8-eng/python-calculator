import csv
FILENAME = "my_books.csv"

def add_book(title, author, year):
    with open(FILENAME, "a" , newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([title, author, year])
def show_books():
    
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            books = list(reader)
    except FileNotFoundError:
        print("файл не найден. Пока что нет книг")
        return

    if not books:
        print("Книг пока нет")
        return

    print("Ваши книги")

    for i, book in enumerate(books, 1):
        title, author, year = book
        print(f"{i}. {title} — {author}, {year}")

def main():
    while True:
        print("\n1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Выход")
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            title = input("Название: ")
            author = input("Автор: ")
            year = input("Год: ")
            add_book(title, author, year)
            print("Книга добавлена")
        elif choice == "2":
            show_books()
        elif choice == "3":
            print("До свидания!")
            break
        else:
            print("Нет такого пункта. Введите 1, 2 или 3")


if __name__ == "__main__":
    main()
