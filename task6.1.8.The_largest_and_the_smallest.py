import ifnumber

print("Наибольшее и наименьшее")
print()

while True:
    num1 = input('Введи число: ')
    if_number = ifnumber.if_number(num1)
    if if_number == 'int':
        num1 = int(num1)
        break
    elif if_number == 'float':
        num1 = float(num1)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    num2 = input('Введи число: ')
    if_number = ifnumber.if_number(num2)
    if if_number == 'int':
        num2 = int(num2)
        break
    elif if_number == 'float':
        num2 = float(num2)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    num3 = input('Введи число: ')
    if_number = ifnumber.if_number(num3)
    if if_number == 'int':
        num3 = int(num3)
        break
    elif if_number == 'float':
        num3 = float(num3)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    num4 = input('Введи число: ')
    if_number = ifnumber.if_number(num4)
    if if_number == 'int':
        num4 = int(num4)
        break
    elif if_number == 'float':
        num4 = float(num4)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()
while True:
    num5 = input('Введи число: ')
    if_number = ifnumber.if_number(num5)
    if if_number == 'int':
        num5 = int(num5)
        break
    elif if_number == 'float':
        num5 = float(num5)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

maximum = max(num1, num2, num3, num4, num5)
minimum = min(num1, num2, num3, num4, num5)

print(f"Из чисел {num1}, {num2}, {num3}, {num4} и  {num5} максимальное - {maximum}, минимальное - {minimum}.")
