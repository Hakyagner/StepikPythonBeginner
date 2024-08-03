import ifnumber
print("Сумма делителей")
print()

while True:
    n = input('Введи число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int':
        n = int(n)
        print()
        break
    elif if_number == 'float':
        n = float(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

total = 0

for i in range(1, n + 1):
    if n % i == 0:
        total += i

print(f"Сумма всех делителей числа {n} ровна {total}.")

# Неправильно
