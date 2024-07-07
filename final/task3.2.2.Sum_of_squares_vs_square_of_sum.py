print("Сумма квадратов VS квадрат суммы")
print()

while True:
    a = input('Введи целое положительное число: ')
    if a.isdigit() or (a[0] == "-" and a[1:].isdigit()):
        a = int(a)
        break
    else:
        print("Нужно вести целое положительное число")
        print()
while True:
    b = input('Введи целое положительное число: ')
    if b.isdigit() or (b[0] == "-" and b[1:].isdigit()):
        b = int(b)
        break
    else:
        print("Нужно вести целое положительное число")
        print()
square_sum = (a + b) ** 2
sum_square = a ** 2 + b ** 2
print()
print(f"Квадрат суммы чисел {a} и {b} равен {square_sum}")
print(f"Сумма квдрата таких чисел {a} и {b} равна {sum_square}")
