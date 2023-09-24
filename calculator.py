import datetime


def calc():
    result = 0

    print("Введите операнды через пробел \n")
    try:
        a, b = map(float, input().split())
    except ValueError as e:
        date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        print(f"[ValueError] - [{e}]: введите два операнда через пробел. Ошибка произошла {date}")
        return

    if a is None or b is None:
        print("Некорректные значения")
        return

    print("Введите оператор \n")
    o = input().strip()

    if o == "+":
        result = a + b
    elif o == "-":
        result = a - b
    elif o == "*":
        result = a * b
    elif o == "/":
        if b == 0:
            print("Делить на ноль нельзя")
            return
        result = a / b
    else:
        print("Такое действие не поддерживается в нашем калькуляторе")
        return

    print(f"Результат вычислений: {result}")

    while True:
        print("Введите операнд или введите Exit")
        a = input()
        if a == "Exit" or a == "exit":
            return
        try:
            a = float(a)
        except ValueError as e:
            date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            print(f"[ValueError] - [{e}]: введеный операнд а некорректного типа. Ошибка произошла {date}")
            return
        print("Введите оператор")
        o = input().strip()

        if o == "+":
            result = result + a
        elif o == "-":
            result = result - a
        elif o == "*":
            result = result * a
        elif o == "/":
            if b == 0:
                print("Делить на ноль нельзя")
                return
            result = result / a
        else:
            print("Такое действие не поддерживается в нашем калькуляторе")
            return

        print(f"Результат вычислений: {result}")