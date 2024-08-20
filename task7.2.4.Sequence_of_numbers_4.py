import ifnumber
print("Последовательность чисел 4")
print()

while True:
    m = input('Введи первое число: ')
    if_number = ifnumber.if_number(m)
    if if_number == 'int' and int(m) > 0:
        m = int(m)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
while True:
    n = input('Введи второе число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
print()

print(f"Целые числа от {m} до {n}:")
for i in range(m, n + 1):
    if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
        print(i)

# m = 20, n = 1. Что будет?
