import ifnumber
print("Таблица-1")
print()

while True:
    n = input('Введи целое число, меньше 9: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) < 9:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число, меньше 9')
        print()

for i in range(n):
    print(n, n, n)
