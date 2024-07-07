print("Принадлежность 2")
print()

while True:
    x = input('Введи целое число: ')
    if x.isdigit() or (x[0] == "-" and x[1:].isdigit()):
        x = int(x)
        break
    else:
        print("Нужно ввести целое число")
        print()
if x <= -3 or x >= 7:
    print(f"Точка с координатой {x} принадлежит промежуткам (-Infiniti, -3) и (7, +Infiniti)")
else:
    print(f"Точка с координатой {x} не принадлежит промежуткам (-Infiniti, -3) и (7, +Infiniti)")
