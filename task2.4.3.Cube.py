import ifnumber
print("Куб")
print()
while True:
    a = input("Напишите длину ребра куба: ")
    if_number = ifnumber.if_number(a)
    if if_number == 'int' and int(a) >= 0:
        a = int(a)
        v = a * a * a
        print("Объём куба =", v)
        s = 6 * a * a
        print("Площадь полной поверхности куба =", s)
        break
    elif if_number == 'float' and int(a) >= 0:
        a = float(a)
        v = a * a * a
        print("Объём куба =", v)
        s = 6 * a * a
        print("Площадь полной поверхности куба =", s)
        break
    else:
        print("Нужно ввести положительное число")
        print()
