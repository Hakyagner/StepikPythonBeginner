import ifnumber
print("Таблица-3")
print()

while True:
    n = input('Введи целое число, меньше или равно 9: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) <= 9:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число, меньше или равно 9')
        print()
print()

for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()

# done
