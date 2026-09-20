import csv
with open ("books_csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Название", "автор", "год"])
    writer.writerow(["у меня нет рта, но я должен кричать", "Харлан Эллисон", "1967"])
    writer.writerow(["82327", "test" , "696969"])

with open("books_csv", "r" , encoding= "utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# with open(filename, "r" , encoding= "utf-8") as file:
#     reader = csv.reader 