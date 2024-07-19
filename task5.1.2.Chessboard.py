print("Шахматная доска")
print()

while True:
    x1 = input('Введи первую координату первой клетки: ')
    if x1.isdigit() and 1 <= int(x1) <= 8:
        x1 = int(x1)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    y1 = input('Введи вторую координату первой клетки: ')
    if y1.isdigit() and 1 <= int(y1) <= 8:
        y1 = int(y1)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    x2 = input('Введи первую координату второй клетки: ')
    if x2.isdigit() and 1 <= int(x2) <= 8:
        x2 = int(x2)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
while True:
    y2 = input('Введи вторую координату второй клетки: ')
    if y2.isdigit() and 1 <= int(y2) <= 8:
        y2 = int(y2)
        break
    else:
        print("Нужно ввести целое положительное число от 1 до 8")
        print()
if abs(x2 - x1) % 2 == 0:
    if abs(y2 - y1) % 2 == 0:
        print(f"Они имеют один и тот же цвет.")
    else:
        print(f"Они не имеют один и тот же цвет.")
else:
    if abs(y2 - y1) % 2 == 0:
        print(f"Они не имеют один и тот же цвет.")
    else:
        print(f"Они имеют один и тот же цвет.")

# Кто или что "они"?