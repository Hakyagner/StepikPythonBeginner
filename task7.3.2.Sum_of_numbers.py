import ifnumber
print("Сумма чисел")
print()

while True:
    num1 = input('Сколько чисел будет введено: ')
    if_number = ifnumber.if_number(num1)
    if if_number == 'int' and int(num1) > 0:
        num1 = int(num1)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
print()

total = 0

for i in range(num1):
    while True:
        num2 = input('Введи целое число: ')
        if_number = ifnumber.if_number(num2)
        if if_number == 'int':
            num2 = int(num2)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
    total += num2

print(total)

# done
