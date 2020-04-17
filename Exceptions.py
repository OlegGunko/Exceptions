def notation():
    while True:
        try:
            a = input("Введите одну из представленных операций: +, -, *, /\n")
            assert a in ("+", "-", "*", "/"), "Данной операции нет"
            x = int(input("Введите первое число: \n"))
            y = int(input("Введите второе число: \n"))
            if x >= 0 and y >= 0:
                if a == "+":
                    print("Результат операции:\n", (lambda x, y: x + y)(x, y))
                elif a == "-":
                    print("Результат операции:\n", (lambda x, y: x - y)(x, y))
                elif a == "*":
                    print("Результат операции:\n", (lambda x, y: x * y)(x, y))
            try:
                if a == "/":
                    print("Результат операции:\n", (lambda x, y: x / y)(x, y))
            except ZeroDivisionError:
                print("На ноль делить нельзя")
            else:
                if x < 0 or y < 0:
                    print("Введите положительное число")
        except ValueError:
            print("Необходимо вводить целое число!")
        except KeyboardInterrupt:
            print("Возможно перед вводом было применено сочетание клавиш Ctrl + C")


notation()
