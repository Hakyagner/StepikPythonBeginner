import ifnumber
from math import *
print("Пол и потолок")
print()

while True:
    x = input('Введите вещественное число в градусах: ')
    if_number = ifnumber.if_number(x)
    if if_number == 'int' or (x[0] == "-" and x[1:].isdigit()):
        x = int(x)
        break
    elif if_number == 'float':
        x = float(x)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

r = radians(x)
total = sin(r) + cos(r) + pow(tan(r), 2)

print(f"Значение [{x}] + [{x}] равна {total}.")
