import ifnumber
print("Последовательность Фибоначчи")
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()

a = 0
b = 1
for i in range(n):
    if n == 1:
        print('1')
    elif n == 2:
        print(1, 1)
    else:
        a, b = b, a + b
        print(a, end=' ')