import ifnumber
print("max и min")
print()

maksim = -1
minim = 10
while True:
    n = input('Введи целое число больше 9: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) >= 10:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число больше 9')
    print()
print()
n1 = n
while n != 0:
    last_digit = n % 10
    if maksim < last_digit:
        maksim = last_digit
    if minim > last_digit:
        minim = last_digit
    n = n // 10

print(f"Максимальная цифра в числе {n1} равна {maksim}.")
print(f"Минимальная цифра в числе {n1} равна {minim}.")
