import ifnumber
print("451 градус по Фаренгейту")
print()

while True:
    f = input("Введите температуру(число) по шкале Цельсия: ")
    if_number = ifnumber.if_number(f)
    if if_number == 'int':
        f = int(f)
        print()
        break
    elif if_number == 'float':
        f = float(f)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число.')
    print()

tc = 5 / 9 * (f - 32)

print(f"{f}°C = {tc}°F")
