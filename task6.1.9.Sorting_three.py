import ifnumber
print("Сортировка трех")
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

maxsim = max(num1, num2, num3)
minimum = min(num1, num2, num3)
print(maxsim)
print((num1 + num2 + num3) - (maxsim + minimum))
print(minimum)

# done
