import ifnumber
from math import floor, ceil

print("Пол и потолок")
print()

while True:
    x = input('Введите число: ')
    if_number = ifnumber.if_number(x)
    if if_number == 'int':
        x = int(x)
        break
    elif if_number == 'float':
        x = float(x)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

total = ceil(x) + floor(x)

print(f"⌊{x}⌋ + ⌈{x}⌉ = {total}")
