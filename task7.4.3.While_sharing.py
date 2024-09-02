import ifnumber
print("Пока делимся")
print()

while True:
    n = input('Введи целое число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int':
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число')
    print()
print()

while n % 7 == 0 and int(n) != 0:
    print(f"Члены данной последовательности {n}")
    while True:
        n = input('Введи целое число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    print()
