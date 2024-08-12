import ifnumber
from math import pi

print("Площадь и длина")
print()

while True:
    r = input("Введите значение радиуса круга: ")
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

print(f"Площадь круга радиуса {r} равна {pi * r ** 2}")
print(f"Длина окружности круга радиуса {r} равна {2 * pi * r}")

# done
