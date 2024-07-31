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

print(f"Первая цифра после точки числа {num} - {num * 10 % 10}.")

# Если ты написала 'Введи целое положительное число: ', это не значит, что нельзя ввести другое. Проверка должна быть правильная