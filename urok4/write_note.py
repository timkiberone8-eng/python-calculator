with open ("note.txt", "a", encoding="utf-8") as file:
    file.write("написал в файл пайтоном \n ")

with open ("note.txt", "a", encoding="utf-8") as file:
    file.write("вторая строка \n ")

note = input("Введите свою заметку: ")
with open("note.txt", "a" , encoding="utf-8") as file:
    file.write(note + "\n")

with open("note.txt", "r" , encoding="utf-8") as file:
    print(file.read())