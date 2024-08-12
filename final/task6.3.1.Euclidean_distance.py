import ifnumber
from math import sqrt
print("Евклидово расстояние")
print()

while True:
    x1 = input("Введите первую координату первой точки: ")
    if_number = ifnumber.if_number(x1)
    if if_number == 'int':
        x1 = int(x1)
        print()
        break
    elif if_number == 'float':
        x1 = float()
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    y1 = input("Введите вторую координату первой точки: ")
    if_number = ifnumber.if_number(y1)
    if if_number == 'int':
        y1 = int(y1)
        print()
        break
    elif if_number == 'float':
        y1 = float(y1)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    x2 = input("Введите первую координату второй точки: ")
    if_number = ifnumber.if_number(x2)
    if if_number == 'int':
        x2 = int(x2)
        print()
        break
    elif if_number == 'float':
        x2 = float(x2)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    y2 = input("Введите вторую координату второй точки: ")
    if_number = ifnumber.if_number(y2)
    if if_number == 'int':
        y2 = int(y2)
        print()
        break
    elif if_number == 'float':
        y2 = float(y2)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

total = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print(f"Евклидово расстояние между двумя точками с координатами ({x1}; {y1}) и ({x2}; {y2}) равно {total}.")
