import ifnumber
print("Дробная часть")
print()

while True:
    num = input('Введи положительное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    elif if_number == 'float' and float(num) > 0:
        num = float(num)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()

total = num % 1

print(f"Дробная часть числа {num} равна {total}.")
