import ifnumber
print("Последовательность чисел 3")
print()
while True:
    print("Нужно ввести два числа, первое число больше второго.")
    while True:
        m = input('Введи первое число: ')
        if_number = ifnumber.if_number(m)
        if if_number == 'int':
            m = int(m)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
    while True:
        n = input('Введи первое число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    if m > n:
        break
    else:
        print('Данные введены некорректно! Первое число больше второго.')
        print()
print()

print(f"Нечётные целые числа от {m} до {n}:")
for i in range(m, n, -1):
    if i % 2 != 0:
        print(i)
