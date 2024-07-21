import ifnumber
print("Куб")
print()

while True:
    a = input('Введи число: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int' and int(a) != 0:
        a = int(a)
        break
    elif if_number == 'float' and int(a) != 0:
        a = float(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

v = a ** 3
print(f"Объём куба = {v}.")
s = 6 * a ** 2
print(f"Площадь полной поверхности = {s}.")

# ЧТО нужно ввести?