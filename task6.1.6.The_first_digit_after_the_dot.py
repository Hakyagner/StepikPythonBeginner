import ifnumber
print("Первая цифра после точки")
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

print(f"Первая цифра после точки числа {num} - {num * 10 % 10}.")

# done