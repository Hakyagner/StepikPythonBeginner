import ifnumber
print("Дробная часть")
print()

while True:
    num = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        print()
        break
    elif if_number == 'float' and int(num) > 0:
        num = float(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()

total = num % 1

print(f"Дробная часть числа {num} равна {total}.")

# Заголовок
# Какое число?
