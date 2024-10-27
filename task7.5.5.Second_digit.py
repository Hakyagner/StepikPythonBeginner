import ifnumber
print("Вторая цифра")
print()

while True:
    n = input('Введи целое положительное число, больше 9: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 9:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число, больше 9.')
        print()
    print()

second_digit = 0
n1 = n
while n > 100:
    n = n // 10

second_digit = n % 10

print(f"Вторая с начала цифра числа {n1} - {second_digit}.")
