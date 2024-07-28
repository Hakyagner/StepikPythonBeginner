import ifnumber

print("Квадрат числа")
print()

while True:
    n = input('Введи число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int':
        n = int(n)
        break
    elif if_number == 'float':
        n = float(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

for i in range(n + 1):
    print(f"Квадрат числа {i} равен {i ** 2}.")

# Какое число нужно ввести?