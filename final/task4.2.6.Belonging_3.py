print("Принадлежность 3")
print()

while True:
    x = input('Введи целое число: ')
    if x.isdigit() or (x[0] == "-" and x[1:].isdigit()):
        x = int(x)
        break
    else:
        print("Нужно ввести целое число")
        print()
if -30 < x <= -2 or 7 < x <= 25:
    print(f"Точка с координатой {x} принадлежит промежуткам (-30, -2) и (7, 25)")
else:
    print(f"Точка с координатой {x} не принадлежит промежуткам (-30, -2) и (7, 25)")
