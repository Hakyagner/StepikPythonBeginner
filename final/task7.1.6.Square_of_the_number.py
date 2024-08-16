import ifnumber

print("Квадрат числа")
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

for i in range(n + 1):
    print(f"Квадрат числа {i} равен {i ** 2}")
