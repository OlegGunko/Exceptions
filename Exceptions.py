def notation():
    while True:
        try:
            value = input("Введите одну из представленных операций: +, -, *, /.\nЗатем введите операнды (числа).\n")
            a, x, y = value.split()
            x, y = int(x), int(y)
            assert a in ("+", "-", "*", "/"), "Данной операции нет"
            if x >= 0 and y >= 0:
                if a == "+":
                    print("Результат операции:\n", (lambda x, y: x + y)(x, y))
                elif a == "-":
                    print("Результат операции:\n", (lambda x, y: x - y)(x, y))
                elif a == "*":
                    print("Результат операции:\n", (lambda x, y: x * y)(x, y))
                elif a == "/":
                    print("Результат операции:\n", (lambda x, y: x / y)(x, y))
            else:
                if x < 0 or y < 0:
                    print("Введите положительное число")
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        except ValueError:
            print("Необходимо вводить целое число!")
        except KeyboardInterrupt:
            print("Возможно перед вводом было применено сочетание клавиш Ctrl + C")



notation()