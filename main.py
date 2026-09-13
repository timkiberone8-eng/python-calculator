# Урок 2, шаг 2. Тот же main.py, но берёт функции уже из ПАКЕТА.
#
# Изменилась ровно одна строка — путь импорта. Всё остальное то же.
# Это полезно показать через git diff: видно, что структура проекта
# поменялась, а логика нет.
#
# Путь читается слева направо как папки:
# calculator_modules (папка) -> operations (пакет) -> basic (файл basic.py)
from calculator_modules.operations.basic import add, subtract, multiply, divide


def main():
    print("Добро пожаловать в калькулятор!")
    a = float(input("Введите первое число: "))
    b = float(input("Введите второе число: "))
    operation = input("Введите операцию (сложение, вычитание, умножение, деление): ").strip().lower()

    if operation == "сложение":
        result = add(a, b)
    elif operation == "вычитание":
        result = subtract(a, b)
    elif operation == "умножение":
        result = multiply(a, b)
    elif operation == "деление":
        result = divide(a, b)
    else:
        result = "Неизвестная операция"

    print(f"Результат: {result}")


if __name__ == "__main__":
    main()
