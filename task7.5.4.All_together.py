import ifnumber
print("Все вместе")
print()

count = 0
mult = 1
total = 0
while True:
    num = input('Введи натуральное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести натуральное число')
        print()

last_digit = num % 10
first_digit = 0
num1 = num
while num != 0:
    digit = num % 10
    total += digit
    count += 1
    mult *= digit
    if num < 10:
        first_digit = num
    num //= 10
print(f"сумма цифр {num1} равна {total}")    # сумма чисел
print(f"Количество цифр в {num1} равна {count}")   # количество чисел
print(f"Произведение цифр {num1} равна {mult}")    # произведение чисел
print(f"Среднее арифметическое цифр {num1} равна {total / count}")   #среднее арифмитическое всех чисел
print(f"Первая цифра числа {num1} - {first_digit}")     # первое число
print(f"Сумма первой и последней цифры числа {num1} равна {first_digit + last_digit}")
