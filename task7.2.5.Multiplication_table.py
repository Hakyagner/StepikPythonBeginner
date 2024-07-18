import ifnumber
print("Таблица умножения")
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

total = 1
for i in range(total, 11):
    i = n * i
    print(f"{n} x {total} = {i}")
    total += 1
