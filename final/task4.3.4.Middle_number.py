print("Серединное число")
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

average = 0
if a < c < b or b < c < a:
    average = c
elif c < b < a or a < b < c:
    average = b
else:
    average = a

print(f"Из чисел {a}, {b} и {c} средним является {average}")
