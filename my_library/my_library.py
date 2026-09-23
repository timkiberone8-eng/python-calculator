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
