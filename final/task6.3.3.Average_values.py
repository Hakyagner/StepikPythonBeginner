import ifnumber
from math import sqrt

print("Средние значения")
print()

while True:
    a = input('Введи первое число: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int':
        a = int(a)
        break
    elif if_number == 'float':
        a = float(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
while True:
    b = input('Введи второе число: ')
    if_number = ifnumber.if_number(b)
    if if_number == 'int':
        b = int(b)
        break
    elif if_number == 'float':
        b = float(b)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

print(f"Среднее арифметическое чисел {a} и {b} равна {(a + b) / 2}.")
print(f"Cреднее геометрическое чисел {a} и {b} равна {sqrt(a * b)}.")
print(f"Cреднее геометрическое чисел {a} и {b} равна {2 * a * b / (a + b)}.")
print(f"Cреднее квадратичное чисел {a} и {b} равна {sqrt((a ** 2 + b ** 2) / 2)}.")
