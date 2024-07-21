import ifnumber
print('Площадь треугольника')
print()

while True:
    a = input("Введите длину первого катета прямоугольного треугольника: ")
    if_number = ifnumber.if_number(a)
    if if_number == 'int' and int(a) != 0:
        a = int(a)
        print()
        break
    elif if_number == 'float' and int(a) != 0:
        a = float(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
while True:
    b = input("Введите длину второго катета прямоугольного треугольника: ")
    if_number = ifnumber.if_number(b)
    if if_number == 'int' and int(b) != 0:
        b = int(b)
        print()
        break
    elif if_number == 'float' and int(b) != 0:
        b = float(b)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
print()
print(f"Площадь треугольника с катетами длиной ({a} и {b}) равна {1 / 2 * a * b}")

# Какое число нужно ввести?
