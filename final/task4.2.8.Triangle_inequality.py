print("Неравенство треугольника")
print()

while True:
    a = input('Введи целое положительное число: ')
    if a.isdigit() and a != 0:
        a = int(a)
        break
    else:
        print("Нужно ввести положительное целое число")
while True:
    b = input('Введи целое положительное число: ')
    if b.isdigit() and b != 0:
        b = int(b)
        break
    else:
        print("Нужно ввести целое положительное число")
while True:
    c = input('Введи целое положиетльное число: ')
    if c.isdigit() and c != 0:
        c = int(c)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()

if a + b > c and a + c > b and b + c > a:
    print(f"Невырожденный треугольник со сторонами {a}, {b} и {c} существует.")
else:
    print(f"Невырожденный треугольник со сторонами {a}, {b} и {c} не существует.")
