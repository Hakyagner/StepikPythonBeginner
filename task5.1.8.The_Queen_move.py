print("Ход ферзя")
print()

while True:
    x1 = input('Введи первую координату клетки, где находится ферзь: ')
    if x1.isdigit() and 1 <= int(x1) <= 8:
        x1 = int(x1)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    y1 = input('Введи вторую координату клетки, где находится ферзь: ')
    if y1.isdigit() and 1 <= int(y1) <= 8:
        y1 = int(y1)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    x2 = input('Введи первую координату клетки, на которорую ферзь должен пойти: ')
    if x2.isdigit() and 1 <= int(x2) <= 8:
        x2 = int(x2)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    y2 = input('Введи вторую координату клетки, на которорую ферзь должен пойти: ')
    if y2.isdigit() and 1 <= int(y2) <= 8:
        y2 = int(y2)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
if (x2 == x1 or y2 == y1) or abs(x2 - x1) == abs(y2 - y1):
    print(f"Ферзь с клетки с координатами ({x1};{y1}) может пойти на клетку с координатами ({x2};{y2})")
else:
    print(f"Слон с клетки с координатами ({x1};{y1}) не может пойти на клетку с координатами ({x2};{y2})")

# Неправильно
