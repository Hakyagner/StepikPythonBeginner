import ifnumber
print("Первая цифра после точки")
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

print(f"Первая цифра от числа {num} после точки - {num * 10 % 10}.")

# done
