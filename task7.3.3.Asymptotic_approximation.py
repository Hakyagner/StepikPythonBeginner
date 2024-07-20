import ifnumber
from math import log
print("Асимптотическое приближение")
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
    total += 1 / (i + 1)

print(f"Разница между накопленной суммой {total} и натуральным логарифмом числа ({n}) = {total - log(n)}.")
