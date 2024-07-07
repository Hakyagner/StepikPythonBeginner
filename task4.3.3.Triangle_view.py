print("Вид треугольника")
print()

while True:
    a = input('Введи целое число: ')
    if a.isdigit() and int(a) > 0:
        a = int(a)
        break
    else:
        print("Нужно ввести целое число")
while True:
    b = input('Введи целое число: ')
    if b.isdigit() and int(b) > 0:
        b = int(b)
        break
    else:
        print("Нужно ввести целое число")
while True:
    c = input('Введи целое число: ')
    if c.isdigit() and int(c) > 0:
        c = int(c)
        break
    else:
        print("Нужно ввести целое число")
        print()

if a == b and c == a:
    print(f"Треугольник со сторонами {a}, {b} и {c} является равносторонним")
elif a != b and c != a and b != c:
    print(f"Треугольник со сторонами {a}, {b} и {c} является разносторонним")
else:
    print(f"Треугольник со сторонами {a}, {b} и {c} является равнобедренным")
