print("Совпадающие числа")
print()

while True:
    a = input('Введи целое число: ')
    if a.isdigit() or (a[0] == "-" and a[1:].isdigit()):
        a = int(a)
        break
    else:
        print("Нужно ввести целое число")
while True:
    b = input('Введи целое число: ')
    if b.isdigit() or (b[0] == "-" and b[1:].isdigit()):
        b = int(b)
        break
    else:
        print("Нужно ввести целое число")
while True:
    c = input('Введи целое число: ')
    if c.isdigit() or (c[0] == "-" and c[1:].isdigit()):
        c = int(c)
        break
    else:
        print("Нужно ввести целое число")
        print()

same = 0

if a == b:
    same += 1
if a == c:
    same += 1
if b == c:
    same += 1
print(f"Из чисел {a}, {b} и {c} одинаковых чисел - {same}")
