import ifnumber
print("Количество пятерок")
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

while 0 < num <= 5:
    total += 1
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
