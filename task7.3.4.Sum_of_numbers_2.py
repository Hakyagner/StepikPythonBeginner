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
    last_digit_square_number = i ** 2 % 10
    if last_digit_square_number == 2 or last_digit_square_number == 5 or last_digit_square_number == 8:
        total += i

print(f"Сумма чисел в диапазоне от 1 до {n}, квадрат которых оканчивается на 2, 5 или 8, равна {total}.")

# done
