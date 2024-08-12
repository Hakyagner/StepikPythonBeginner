import ifnumber
print("Манхэттенское расстояние")
print()

while True:
    p1 = input('Введи первую координату первой точки: ')
    if_number = ifnumber.if_number(p1)
    if if_number == 'int':
        p1 = int(p1)
        break
    elif if_number == 'float':
        p1 = float(p1)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    p2 = input('Введи вторую координату первой точки: ')
    if_number = ifnumber.if_number(p2)
    if if_number == 'int':
        p2 = int(p2)
        break
    elif if_number == 'float':
        p2 = float(p2)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    q1 = input('Введи первую координату второй точки: ')
    if_number = ifnumber.if_number(q1)
    if if_number == 'int':
        q1 = int(q1)
        break
    elif if_number == 'float':
        q1 = float(q1)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    q2 = input('Введи вторую координату второй точки: ')
    if_number = ifnumber.if_number(q2)
    if if_number == 'int':
        q2 = int(q2)
        break
    elif if_number == 'float':
        q2 = float(q2)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

total = abs(p1 - q1) + abs(p2 - q2)
print(f"Манхэттенское расстояние между двумя точками с координатами ({p1}, {p2}), ({q1}, {q2}) равно {total}.")

# done
