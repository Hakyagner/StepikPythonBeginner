import ifnumber
print("Количество пятерок")
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

while 0 < n < 6:
    if n == 5:
        total += 1
    while True:
        n = input('Введи целое число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()

print(f"Количество пятерок в данной последовательности {total}")

# Какая последовательность?
