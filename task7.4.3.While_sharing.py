import ifnumber
print("Пока делимся")
print()

while True:
    num = input('Введи число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int':
        num = int(num)
        print()
        break
    elif if_number == 'float':
        num = float(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

while num % 7 == 0:
    print(num)
    while True:
        num = input('Введи число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int':
            num = int(num)
            print()
            break
        elif if_number == 'float':
            num = float(num)
            break
        else:
            print('Данные введены некорректно! Нужно ввести число')
        print()
