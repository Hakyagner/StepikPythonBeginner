import ifnumber
print("Последовательность чисел 1")
print()

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
print()

if m < n:
    for i in range(m, n + 1):
        print(f"Целые числа от {m} до {n} (включительно) - {i}.")
else:
    for i in range(n, m + 1):
        print(f"Целые числа от {n} до {m} (включительно) - {i}.")
