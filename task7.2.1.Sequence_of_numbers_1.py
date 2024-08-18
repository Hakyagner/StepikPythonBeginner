import ifnumber
print("Последовательность чисел 1")
print()

while True:
    print("Нужно ввести два целых числа. Второе число должно быть не меньше первого.")
    while True:
        m = input('Введи первое число: ')
        if_number = ifnumber.if_number(m)
        if if_number == 'int':
            m = int(m)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
    while True:
        n = input('Введи второе число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    if m <= n:
        break
    else:
        print('Данные введены некорректно! Второе число должно быть не меньше первого.')
    print()
print()

print(f"Целые числа от {m} до {n}")
for i in range(m, n + 1):
    print(i)

# Неправильно. Но по условию задачи m ≤ n
