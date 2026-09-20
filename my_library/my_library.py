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

        if not books:
            print("файл не найден. Пока что нет книг")
            return

        print("Ваши книги")

        for i, books in enum(books, i)
        