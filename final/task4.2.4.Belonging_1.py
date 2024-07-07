print("Принадлежность 1")
print()

while True:
    x = input('Введи целое число: ')
    if x.isdigit() or (x[0] == "-" and x[1:].isdigit()):
        x = int(x)
        break
    else:
        print("Нужно ввести целое число")
        print()
print()
if -1 < x < 17:
    print(f"Точка с координатой {x} принадлежит промежутку (-1, 17)")
else:
    print(f"Точка с координатой {x} не принадлежит промежутку (-1, 17)")

# print(f"Точка с координатой {x} ", end="")
# if not -1 < x < 17:
#     print("не ", end="")
# print("принадлежит промежутку (-1, 17)")
