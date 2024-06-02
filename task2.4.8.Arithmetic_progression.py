print("Арифметическая прогрессия")
print()
while True:
    a1 = input("Введите первый член арифметической прогресcии: ")
    if a1.isdigit():
        a1 = int(a1)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    d = input("Введите разность арифметической прогрессии: ")
    if d.isdigit():
        d = int(d)
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
an = a1 + d * (n - 1)
print(an)

# Переменные не определены до цикла