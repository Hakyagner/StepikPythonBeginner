import ifnumber
print("Последовательность чисел 3")
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

for i in range(m, n, -2):
    if i % 2 != 0:
        print(f"Все нечётные целые числа от {m} до {n} (включительно) - {i}")

# Неправильно