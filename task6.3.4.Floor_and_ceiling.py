import ifnumber
from math import floor, ceil

print("Пол и потолок")
print()

while True:
    x = input('Введите положительное число: ')
    if_number = ifnumber.if_number(x)
    if if_number == 'int' and int(x) > 0:
        x = int(x)
        break
    elif if_number == 'float' and float(x) > 0:
        x = float(x)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()

total = ceil(x) + floor(x)

print(f"{x} + {x} = {total}")

# done
