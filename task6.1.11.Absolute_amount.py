import ifnumber
print("Абсолютная сумма")
print()

while True:
    a1 = input('Введи первое число: ')
    if_number = ifnumber.if_number(a1)
    if if_number == 'int':
        a1 = int(a1)
        break
    elif if_number == 'float':
        a1 = abs(float(a1))
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
while True:
    a2 = input('Введи второе число: ')
    if_number = ifnumber.if_number(a2)
    if if_number == 'int':
        a2 = int(a2)
        break
    elif if_number == 'float':
        a2 = abs(float(a2))
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
while True:
    a3 = input('Введи третье число: ')
    if_number = ifnumber.if_number(a3)
    if if_number == 'int':
        a3 = int(a3)
        break
    elif if_number == 'float':
        a3 = abs(float(a3))
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
while True:
    a4 = input('Введи четвёртое число: ')
    if_number = ifnumber.if_number(a4)
    if if_number == 'int':
        a4 = int(a4)
        break
    elif if_number == 'float':
        a4 = abs(float(a4))
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
while True:
    a5 = input('Введи пятое число: ')
    if_number = ifnumber.if_number(a5)
    if if_number == 'int':
        a5 = int(a5)
        break
    elif if_number == 'float':
        a5 = abs(float(a5))
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

total = abs(a1) + abs(a2) + abs(a3) + abs(a4) + abs(a5)

print(f"Сумма чисел модуля {a1}, {a2}, {a3}, {a4}, {a5} ровна {total}.")

# Сравни, например, строки 56 и 62. В чем ошибка?
# Русский язык при выводе. Читай условие задачи. Поможет
