import ifnumber

print("Интересное число")
print()

while True:
    abc = input('Введи число: ')
    if_number = ifnumber.if_number(abc)
    if if_number == 'int' and 100 <= int(abc) <= 999:
        break
    elif if_number == 'float' and 100 <= float(abc) <= 999:
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

maximum = max(abc[0], abc[1], abc[2])
minimum = min(abc[0], abc[1], abc[2])

if (minimum == abc[2] and maximum == abc[0]) or (minimum == abc[0] and maximum == abc[2]):
    if int(maximum) - int(minimum) == int(abc[1]):
        print(f"У Числа {abc} равняется разность максимальной и минимальной цифры средней по величине цифре.")
    else:
        print(f"У Числа {abc} не равняется разность максимальной и минимальной цифры средней по величине цифре.")
elif (minimum == abc[1] and maximum == abc[2]) or (minimum == abc[2] and maximum == abc[1]):
    if int(maximum) - int(minimum) == int(abc[0]):
        print(f"У Числа {abc} равняется разность максимальной и минимальной цифры средней по величине цифре.")
    else:
        print(f"У Числа {abc} не равняется разность максимальной и минимальной цифры средней по величине цифре.")
elif (minimum == abc[1] and maximum == abc[0]) or (minimum == abc[0] and maximum == abc[1]):
    if int(maximum) - int(minimum) == int(abc[0]):
        print(f"У Числа {abc} равняется разность максимальной и минимальной цифры средней по величине цифре.")
    else:
        print(f"У Числа {abc} не равняется разность максимальной и минимальной цифры средней по величине цифре.")
else:
    print("Ошибка код введён не коректно.")

# done
