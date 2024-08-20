import ifnumber
print("Последовательность чисел 2")
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
    print(f"Целые числа от {m} до {n}:")
    for i in range(m, n + 1):
        print(i)
else:
    print(f"Целые числа от {m} до {n}:")
    for i in range(m, n - 1, -1):
        print(i)

# done
