print("Геометрическая прогрессия")
print()
while True:
    b1 = input("Введи первый член геометрической прогрессии: ")
    if b1.isdigit() or (b1[0] == "-" and b1[1:].isdigit()):
        b1 = int(b1)
        break
    else:
        print("Нужно ввести целое число")
        print()
while True:
    q = input("Введи знаменатель геометрической прогрессии: ")
    if (q.isdigit() or (q[0] == "-" and q[1:].isdigit())) and int(q) != 0:
        q = int(q)
        break
    else:
        print("Нужно ввести целое число, не равное 0")
        print()
while True:
    n = input("Введите номер члена геометрической прогрессии, который нужно найти: ")
    if n.isdigit() and int(n) >= 1:
        n = int(n)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
bn = b1 * q ** (n - 1)
print()
print(f"{n}-ый член геометрической прогрессии, в которой первое число = {b1}, знаменатель прогрессии = {q}, равен {bn}")
