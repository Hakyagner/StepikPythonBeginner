print("Ход короля")
print()

while True:
    x1 = input('Введи первую координату клетки, где находится ладья: ')
    if x1.isdigit() and 1 <= int(x1) <= 8:
        x1 = int(x1)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    y1 = input('Введи вторую координату клетки, где находится ладья: ')
    if y1.isdigit() and 1 <= int(y1) <= 8:
        y1 = int(y1)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    x2 = input('Введи первую координату клетки, куда ладья должна пойти: ')
    if x2.isdigit() and 1 <= int(x2) <= 8:
        x2 = int(x2)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    y2 = input('Введи вторую координату клетки, куда ладья должна пойти: ')
    if y2.isdigit() and 1 <= int(y2) <= 8:
        y2 = int(y2)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()

if ((x2 - x1 == -1 or x2 - x1 == 1) and (y2 == y1 or y2 - y1 == 1 or y2 - y1 == -1)) or (x2 == x1 and (y2 - y1 == 1 or y2 - y1 == -1)):
    print(f"Король с клетки с координатами ({x1};{y1}) может пойти на клетку с координатами ({x2};{y2})")
else:
    print(f"Король с клетки с координатами ({x1};{y1}) не может пойти на клетку с координатами ({x2};{y2})")