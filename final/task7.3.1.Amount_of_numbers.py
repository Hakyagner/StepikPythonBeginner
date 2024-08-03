import ifnumber
print("Количество чисел")
print()

while True:
    a = input('Введи первое целое число: ')
    if_number = ifnumber.if_number(a)
    if if_number == 'int':
        a = int(a)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число')
while True:
    b = input('Введи первое целое число: ')
    if_number = ifnumber.if_number(b)
    if if_number == 'int':
        b = int(b)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число')
    print()
print()

total = 0

for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        total += 1

print(f"Количество чисел в диапазоне от {a} до {b} (включительно), куб которых оканчивается на 4 или 9, равно {total}.")
