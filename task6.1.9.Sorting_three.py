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

maximum = max(num1, num2, num3)
minimum = min(num1, num2, num3)

if minimum == num3 and maximum == num1:
    print(maximum, num2, minimum)
elif minimum == num1 and maximum == num3:
    print(maximum, num2, minimum)
elif minimum == num2 and maximum == num3:
    print(maximum, num1, minimum)
elif (minimum == num2 and maximum == num3) or (minimum == num3 and maximum == num2):
    print(maximum, num1, minimum)
elif (minimum == num2 and maximum == num1) or (minimum == num1 and maximum == num2):
    print(maximum, num3, minimum)

# Вывод не оптимизирован
# Для более простого решения: что будет, если из суммы всех чисел вычесть максимально и минимальное?