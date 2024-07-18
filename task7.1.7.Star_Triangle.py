import ifnumber
print("Звёздный треугольник")
print()

while True:
    n = input('Введи число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and n == 11:
        n = int(n)
        break
    elif if_number == 'float' and n == 11:
        n = float(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число каторое равно  11.')
    print()

for i in range(n):
    print("*" * (n - i))
