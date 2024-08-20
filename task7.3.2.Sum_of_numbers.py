import ifnumber
print("Сумма чисел")
print()

while True:
    n = input('Введи целое положительное число: ')
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
        n_n = input('Введи целое число: ')
        if_number = ifnumber.if_number(n_n)
        if if_number == 'int':
            n_n = int(n_n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
    total += n_n

print(total)

# done
