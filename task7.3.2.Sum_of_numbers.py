import ifnumber
print("Сумма чисел")
print()

while True:
    n = input('Введи число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int':
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число')
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

# Подумай, что такое n. Что нужно спросить у пользователя? И каким должно быть n?