import ifnumber
print("Сумма чисел")
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

total = 0

while num > -1:
    total += num
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
print(total)
