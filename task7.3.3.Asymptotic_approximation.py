import ifnumber
from math import log
print("Асимптотическое приближение")
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
print()

total = 0

for i in range(n):
    total += 1 / (i + 1)

print(f"Разница между накопленной суммой {total} и натуральным логарифмом числа ({n}) = {total - log(n)}")

# неправильно. Внимательно читай условие задачи
