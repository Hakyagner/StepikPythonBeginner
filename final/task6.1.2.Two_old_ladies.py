import ifnumber
print("Две старушки")
print()

while True:
    v1 = input("Введите скорость первой старушки: ")
    if_number = ifnumber.if_number(v1)
    if if_number == 'int' and int(v1) > 0:
        v1 = int(v1)
        print()
        break
    elif if_number == 'float' and int(v1) > 0:
        v1 = float(v1)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
while True:
    v2 = input("Введите скорость второй старушки: ")
    if_number = ifnumber.if_number(v2)
    if if_number == 'int' and int(v2) > 0:
        v2 = int(v2)
        print()
        break
    elif if_number == 'float' and int(v2) > 0:
        v2 = float(v2)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
while True:
    s = input("Введите расстояние между старушками: ")
    if_number = ifnumber.if_number(s)
    if if_number == 'int' and int(s) > 0:
        s = int(s)
        print()
        break
    elif if_number == 'float' and int(s) > 0:
        s = float(s)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')

t = (v1 + v2) / s
print(f"Старушки, расстояние между которыми {s}, и идущие на встречу к друг другу со скоростями {v1} и {v2}, встретятся через {t} часов.")
