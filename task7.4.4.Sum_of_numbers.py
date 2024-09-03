import ifnumber
print("Сумма чисел")
print()


while True:
    n = input('Введи целое число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int':
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число')
    print()
print()

total = 0
while n >= 0:
    total += n
    while True:
        n = input('Введи целое число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    print()

print(f"Сумма всех членов данной последовательности рана {total}")

# В нагрузку: выведи последовательность. Ты уже умеешь