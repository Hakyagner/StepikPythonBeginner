import ifnumber
print("451 градус по Фаренгейту")
print()

while True:
    f = float("Введите температуру(число) по шкале Цельско: ")
    if_number = ifnumber.if_number(f)
    if if_number == 'int' and int(f) > 0:
        f = int(f)
        print()
        break
    elif if_number == 'float' and int(f) > 0:
        f = float(f)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число.')
    print()

tc = 5 / 9 * (f - 32)

print(f"Температура по шкале Цельско {f} соответствует значению градусовпо {tc} щколе Фаренгейта")

# Добавь проверку числа.
# Внимательно читай условие задачи. Часто это помогает с русским языком