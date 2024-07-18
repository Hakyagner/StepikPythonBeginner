print("Пересечение отрезков")
print()

while True:
    a1 = input('Введи первую координату первого отрезка: ')
    if a1.isdigit() or (a1[0] == "-" and a1[1:].isdigit()):
        a1 = int(a1)
        break
    else:
        print("Нужно ввести целое число")
while True:
    b1 = input('Введи вторую координату первого отрезка: ')
    if b1.isdigit() or (b1[0] == "-" and b1[1:].isdigit()):
        b1 = int(b1)
        break
    else:
        print("Нужно ввести целое число")
while True:
    a2 = input('Введи первую координату второго отрезка: ')
    if a2.isdigit() or (a2[0] == "-" and a2[1:].isdigit()):
        a2 = int(a2)
        break
    else:
        print("Нужно ввести целое число")
while True:
    b2 = input('Введи вторую координату второго отрезка: ')
    if b2.isdigit() or (b2[0] == "-" and b2[1:].isdigit()):
        b2 = int(b2)
        break
    else:
        print("Нужно ввести целое число")

if a1 > b1:
    a1, b1 = b1, a1
if a2 > b2:
    a2, b2 = b2, a2
if a1 > a2:
    a1, a2, b1, b2 = a2, a1, b2, b1

if b1 < a2:
    print(f"Отрезки с координатами [{a1}; {b1}] и [{a2}; {b2}] не пересекаются.")
elif b1 == a2:
    print(f"Отрезки с координатами [{a1}; {b1}] и [{a2}; {b2}] имеют одну общую точку {a2}.")
elif a1 <= a2:
    if b1 < b2:
        print(f"Пересечение отрезков с координатами [{a1}; {b1}] и [{a2}; {b2}] образуют отрезок [{a2}; {b1}].")
    else:
        print(f"Пересечение отрезков с координатами [{a1}; {b1}] и [{a2}; {b2}] образуют отрезок [{a2}; {b2}].")
