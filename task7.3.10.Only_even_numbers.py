import ifnumber
print("Only even numbers")
print()

total = 0
for i in range(10):
    while True:
        num = input('Введи целое положительное число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' and int(num) > 0:
            num = int(num)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
    if num % 2 == 0:
        total += 1
if total == 10:
    print('YES')
else:
    print('NO')
