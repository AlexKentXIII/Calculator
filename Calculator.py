import math


def sum(a, b):
    if ((a + b) - math.floor(a + b)) != 0:
        return f'Ответ {a + b}'
    else:
        return f'{int(a + b)}'


def dif(a, b):
    if ((a + b) - math.floor(a - b)) != 0:
        return f'Ответ {a - b}'
    else:
        return f'{int(a - b)}'


def div(a, b):
    if ((a / b) - math.floor(a / b)) != 0:
        return f'Ответ {a / b}'
    else:
        return f'{int(a / b)}'


def mul(a, b):
    if ((a * b) - math.floor(a * b)) != 0:
        return f'Ответ {a * b}'
    else:
        return f'{int(a * b)}'


def exp(a, b):
    if ((a ** b) - math.floor(a ** b)) != 0:
        return f'Ответ {a ** b}'
    else:
        return f'{int(a ** b)}'


signs = ['+', '-', '/', '**', '*']

print('''Добро пожаловать в калькулятор.
Доступные операции: сложение (+), вычитание(-), умножение(*), деление(/), возведение 1-го числа в степень 2-го (**) ''')
while True:
    try:
        a = float(input('Введите число 1\n'))
    except(ValueError):
        print('Необходимо вводить цифры')
        continue
    s = input('Операция\n')
    if s not in signs:
        print('Вторым нужно ввести знак операции')
        continue
    try:
        b = float(input('Введите число 2\n'))
    except(ValueError):
        print('Необходимо вводить цифры')
        continue

    if s == '+':
        print(sum(a, b))
    if s == '-':
        print(dif(a, b))
    if s == '/':
        print(div(a, b))
    if s == '*':
        print(mul(a, b))
    if s == '**':
        print(exp(a, b))
