import ifnumber
from math import tan, pi

print("Правильный многоугольник")
print()

while True:
    a = input('Введи длину стороны правильного многоугольника: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int':
        a = int(a)
        break
    elif if_number == 'float':
        a = float(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    n = input('Введи количество сторон правильного многоугольника: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int':
        n = int(n)
        break
    elif if_number == 'float':
        n = float(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

s = (n * a ** 2) / (4 * tan(pi / n))

print(f"Площадь правильного прямоугольника равна {s}.")

# done
