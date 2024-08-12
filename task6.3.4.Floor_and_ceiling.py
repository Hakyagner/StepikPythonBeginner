import ifnumber
from math import sin, tan, cos, radians

print("Пол и потолок")
print()

while True:
    x = input('Введите вещественное число: ')
    if_number = ifnumber.if_number(x)
    if if_number == 'int' and int(x) > 0:
        x = int(x)
        break
    elif if_number == 'float' and int(x) > 0:
        x = float(x)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()

r = radians(x)
total = sin(r) + cos(r) + pow(tan(r), 2)

print(f"Значение [{x}] + [{x}] равна {total}.")

# совсем не та задача
# Какое число нужно ввести?
# Русский язык
