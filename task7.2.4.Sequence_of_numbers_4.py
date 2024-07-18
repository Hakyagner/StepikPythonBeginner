import ifnumber
print("Последовательность чисел 4")
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

for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(f"Целые числа от {m} до {n} (включительно) - {i}.")
