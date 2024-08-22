import ifnumber
print("Сумма чисел")
print()

while True:
    n = input('Сколько чисел будет введено? ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
print()

total = 0

for i in range(n):
    while True:
        num = input('Введи целое число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int':
            num = int(num)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
    total += num

print(total)
