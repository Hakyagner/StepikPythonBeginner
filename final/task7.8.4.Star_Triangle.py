import ifnumber
print("Звёздный треугольник")
print()

while True:
    n = input('Введи целое положительное нечётное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) % 2 != 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное нечётное число')
        print()

print()
print(f"Равнобедренный звёздный треугольник с основанием, равным {n}:")
print()
for i in range(1, n + 1):
    for j in range(i):
        if i + j > n:
            continue
        print('*', end='')
    print()
