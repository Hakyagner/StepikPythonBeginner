print("Координатная четверть")
print()

while True:
    x = input('Введи целое число, не равное 0: ')
    if x.isdigit() or (x[0] == "-" and x[1:].isdigit()) and int(x) != 0:
        x = int(x)
        break
    else:
        print("Нужно ввести целое число не равное 0")
        print()
while True:
    y = input('Введи целое число, не равное 0: ')
    if y.isdigit() or (y[0] == "-" and y[1:].isdigit()) and int(y) != 0:
        y = int(y)
        break
    else:
        print("Нужно ввести целое число не равное 0")
        print()
if x > 0 and y > 0:
    print(f"Точка с координатами ({x}; {y}) находится в 1 координатной четверти")
elif x < 0 and y > 0:
    print(f"Точка с координатами ({x}; {y}) находится во 2 координатной четверти")
elif x < 0 and y < 0:
    print(f"Точка с координатами ({x}; {y}) находится в 3 координатной четверти")
elif x > 0 and y < 0:
    print(f"Точка с координатами ({x}; {y}) находится в 4 координатной четверти")
