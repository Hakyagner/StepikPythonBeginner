import ifnumber
print("Таблица-2")
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

for i in range(1, n + 1):
    print(i, i, i, i, i)

# Если вдруг надо писать ещё что-то в print, то подскажи что надо !