import ifnumber
from math import tan, pi

print("Правильный многоугольник")
print()

while True:
    n = input('Введи количество сторон правильного многоугольника: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 2:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число больше 2')
    print()
while True:
    a = input('Введи длину стороны правильного многоугольника: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int' and int(a) > 0:
        a = int(a)
        break
    elif if_number == 'float' and float(a) > 0:
        a = float(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()

s = (n * a ** 2) / (4 * tan(pi / n))

print(f"Площадь правильного прямоугольника с длиной стороны {a} и количеством сторон {n} равна {s}.")

# done
