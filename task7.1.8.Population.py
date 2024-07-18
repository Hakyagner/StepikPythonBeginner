import ifnumber
print("Популяция")
print()

while True:
    m = input('Введи стартовое количество организмов: ')
    if_number = ifnumber.if_number(m)
    if if_number == 'int' and int(m) > 0:
        m = int(m)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
while True:
    p = input('Введи среднесуточное увеличение в %: ')
    if_number = ifnumber.if_number(p)
    if if_number == 'int' and int(p) > 0:
        p = int(p)
        break
    elif if_number == 'float' and float(p) > 0:
        p = float(p)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
while True:
    n = input('Введи количество дней: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()

for i in range(1, n + 1):
    print(f"Размер популяции организмов в {i + 1} день ровна {m}.")
    m = m * (1 + p / 100) ** (n - 1)

