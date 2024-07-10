print("Арифметическая прогрессия")
print()
while True:
    a1 = input("Введите первый член арифметической прогресcии: ")
    if a1.isdigit() or (a1[0] == "-" and a1[1:].isdigit()):
        a1 = int(a1)
        break
    else:
        print("Нужно ввести целое число")
        print()
while True:
    d = input("Введите разность арифметической прогрессии: ")
    if d.isdigit() or (d[0] == "-" and d[1:].isdigit()):
        d = int(d)
        break
    else:
        print("Нужно ввести целое число")
        print()
while True:
    n = input("Какой член арифметической прогрессии нужно найти? ")
    if n.isdigit() and int(n) >= 1:
        n = int(n)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
an = a1 + d * (n - 1)
print()
print(f"{n}-ый член арифметической прогрессии, в которой первое число равно {a1} и разность прогрессии равна {d}, равен {an}")
