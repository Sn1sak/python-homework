def calc(n_1, n_2, op):
    """Function evaluates the expression and prints the result"""
    if op == '+':
        print(n_1 + n_2)
    elif op == '-':
        print(n_1 - n_2)
    elif op == '*':
        print(n_1 * n_2)
    elif op == '/':
        if n_2 == 0:
            raise ZeroDivisionError
        print(n_1 / n_2)
    elif op == '^':
        print(n_1 ** n_2)
    elif op == 'sqrt':
        if n_2 == 0:
            print("1")
            return
        print(pow(n_1, 1 / n_2))
    elif op == '%':
        print(n_1 % n_2)
    elif op == '//':
        print(n_1 // n_2)
    else:
        print('Вы не выбрали действие.')


try:
    num_1 = float(input('Введите первое число: '))
    num_2 = float(input('Введите второе число: '))
    operator = input('Выберите действие ( + | - | * | / | ^ | sqrt | % | // ): ')
    calc(num_1, num_2, operator)
except TypeError:
    print('Вы ввели некорректные данные')
except ZeroDivisionError:
    print('Деление на 0')
except KeyboardInterrupt:
    print('Выход из программы')
