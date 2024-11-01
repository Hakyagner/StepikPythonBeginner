import ifnumber

print("Одинаковые цифры")
print()

while True:
    num = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    elif if_number == 'float':
        num = float(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число.')
        print()
    print()

num1 = num
last_digit = num % 10
flag = True

while num != 0:
    if last_digit != num % 10:
        flag = False
        break
    num = num // 10
if flag:
    print(f"В числе {num1} все цифры одинаковые.")
else:
    print(f"В числе {num1} цифры не одинаковые.")
