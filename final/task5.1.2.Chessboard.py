print("Шахматная доска")
print()

while True:
    x1 = input('Введи первую координату первой клетки шахматной доски: ')
    if x1.isdigit() and 1 <= int(x1) <= 8:
        x1 = int(x1)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    y1 = input('Введи вторую координату первой клетки шахматной доски: ')
    if y1.isdigit() and 1 <= int(y1) <= 8:
        y1 = int(y1)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    x2 = input('Введи первую координату второй клетки шахматной доски: ')
    if x2.isdigit() and 1 <= int(x2) <= 8:
        x2 = int(x2)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    y2 = input('Введи вторую координату второй клетки шахматной доски: ')
    if y2.isdigit() and 1 <= int(y2) <= 8:
        y2 = int(y2)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
if (x1 + y1 + x2 + y2) % 2 == 0:
    print(f"У клеток шахматной доски с координатами ({x1};{y1}) и ({x2};{y2}) одинаковый цвет.")
else:
    print(f"У клеток шахматной доски с координатами ({x1};{y1}) и ({x2};{y2}) не одинаковый цвет.")
