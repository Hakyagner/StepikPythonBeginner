import ifnumber
from math import pi
print("Площадь и длина")
print()

while True:
    r = input("Введите значение радиоса: ")
    if_number = ifnumber.if_number(r)
    if if_number == 'int':
        r = int(r)
        break
    elif if_number == 'float':
        r = float(r)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

print(f"Площадь круга окружности по заданному радиусу {r} равна {pi * r ** 2}.")
print(f"Длина круга окружности по заданному радиусу {r} ровна {2 * pi * r}.")
