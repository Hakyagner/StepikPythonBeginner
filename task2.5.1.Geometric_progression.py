print("Геометрическая прогрессия")
print()
while True:
    b1 = input("Введи первое число геометрической прогрессии: ")
    if b1.isdigit():
        b1 = int(b1)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    q = input("Введи знаменатель прогрессии: ")
    if q.isdigit():
        q = int(q)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    n = input("Введите номер члена арифметической прогрессии, который нужно найти: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
bn = b1 * q ** (n - 1)
print(bn)
print()

# Вывод непонятен