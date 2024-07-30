import ifnumber
print("Дробная часть")
print()

while True:
    num = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int':
        num = int(num)
        print()
        break
    elif if_number == 'float':
        num = float(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()

total = num % 1

print(f"Дробная часть числа {num} равна {total}.")

# done
