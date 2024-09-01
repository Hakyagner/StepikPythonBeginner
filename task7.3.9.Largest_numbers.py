import ifnumber
print("Наибольшие числа")
print()

while True:
    num = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
print()

maximum1 = 0
maximum2 = 0

for i in range(num):
    while True:
        n = input('Введи целое положительное число: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int' and int(n) > 0:
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()
    if n > maximum2:
        maximum2 = n
    if maximum2 >= maximum1:
        maximum2, maximum1 = maximum1, maximum2

print(f"Наибольшее число - {maximum1}")
print(f"Второе наибольшее число последовательности - {maximum2}")

# Решение правильное, но есть нюансы
# Что нужно спросить, чтобы пользователю было понятно, что от него требуется в самом начале?
# Переделай ввод чисел так, чтобы было понятно, какое по счёту число вводится