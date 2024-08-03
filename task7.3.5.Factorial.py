import ifnumber
print("Факториал")
print()

while True:
    n = input('Введи число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int':
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число')
    print()
print()

total = 0

for i in range(1, n + 1):
    total *= i

print(f"{n}! = {total}.")

# Требования к числу?
# Неверное решение