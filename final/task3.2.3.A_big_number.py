print('Большое число')
print()
while True:
    a = input('Введи целое положительное число: ')
    if a.isdigit():
        a = int(a)
        break
    else:
        print("Нужно вести целое положительное число")
        print()

while True:
    b = input('Введи целое положительное число: ')
    if b.isdigit():
        b = int(b)
        break
    else:
        print("Нужно вести целое положительное число")
        print()
while True:
    c = input('Введи целое положительное число: ')
    if c.isdigit():
        c = int(c)
        break
    else:
        print("Нужно вести целое положительное число")
        print()
while True:
    d = input('Введи целое положительное число: ')
    if d.isdigit():
        d = int(d)
        break
    else:
        print("Нужно вести целое положительное число")
        print()
total = a ** b + c ** d
print(total)
