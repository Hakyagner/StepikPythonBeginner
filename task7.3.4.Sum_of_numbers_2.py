import ifnumber
print("Сумма чисел 2")
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

for i in range(1, n + 1):
    if i ** 2 % 10 == 2 or i ** 3 % 10 == 5 or i ** 3 % 10 == 8:
        total += 1

print(f"Количество чисел в диапазоне от 1 до {n} (включительно), квадрат которых оканчивается на 2, 5 или 8 равно {total}.")

# done
