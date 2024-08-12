import ifnumber
from math import pi

print("Площадь и длина")
print()

while True:
    r = input("Введите значение радиуса: ")
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

print(f"{pi * r ** 2}")
print(f"{2 * pi * r}")

# Приучаем к математике: радиус есть у всех фигур?
# Пожалуйста, полный вывод. Иначе зачем тебе print(f"") нужен?
