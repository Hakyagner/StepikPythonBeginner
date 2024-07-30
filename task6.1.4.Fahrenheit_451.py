import ifnumber
print("451 градус по Фаренгейту")
print()

while True:
    f = float("Введите температуру(число) по шкале Цельско: ")
    if_number = ifnumber.if_number(f)
    if if_number == 'int' or (f[0] == "-" and f[1:].isdigit()) and int(f) > 0:
        f = int(f)
        print()
        break
    elif if_number == 'float' and int(f) > 0:
        f = float(f)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число.')
    print()

tc = 5 / 9 * (f - 32)

print(f"Температура по шкале Цельска {f} соответствует значению градусов по {tc} щколе Фаренгейта")

# done