print("Куб")
print()
while True:
    a = input("Напишите длину ребра куба: ")
    if a.isdigit():
        a = int(a)
        v = a * a * a
        print("Объём куба =", v)
        s = 6 * a * a
        print("Площадь полной поверхности куба =", s)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
