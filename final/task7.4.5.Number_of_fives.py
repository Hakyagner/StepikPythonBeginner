import ifnumber
print("Количество пятерок")
print()

all_s = ""
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
    if all_s == "":
        all_s += str(n)
    else:
        all_s += ", " + str(n)
    while True:
        n = input('Введи целое число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()

print(f"Количество пятерок в последовательности ({all_s}) равно {total}.")
