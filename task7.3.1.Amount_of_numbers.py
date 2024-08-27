import ifnumber
print("Количество чисел")
print()
while True:
    print("Нужно ввести два целых числа, первое число не больше второго.")
    while True:
        a = input('Введи первое целое число: ')
        if_number = ifnumber.if_number(a)
        if if_number == 'int':
            a = int(a)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
    while True:
        b = input('Введи второе целое число: ')
        if_number = ifnumber.if_number(b)
        if if_number == 'int':
            b = int(b)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    if a <= b:
        break
    else:
        print('Данные введены некорректно! Первое число должно быть не больше второго.')
print()

total = 0

for i in range(a, b + 1):
    if i ** 3 % 10 == 4 or i ** 3 % 10 == 9:
        total += 1

print(f"Количество чисел в диапазоне от {a} до {b}, куб которых оканчивается на 4 или 9 - {total}.")

# i ** 3 % 10 - вычисления делаются 2 раза. Оптимизируй
