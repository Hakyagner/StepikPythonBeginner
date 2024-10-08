import ifnumber
print("Знакочередующаяся сумма")
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

for i in range(1, n + 1):
    if i % 2 == 0:
        total -= i
    else:
        total += i

if n <= 5:
    s = '1'
    sep = ''
    for i in range(2, n + 1):
        if i % 2 == 0:
            sep = ' - '
        else:
            sep = ' + '
        s = s + sep + str(i)
    print(f'{s} = {total}')
else:
    print(f"1 − 2 + 3 − 4 + … + (−1)^{n + 1} * {n} = {total}")
