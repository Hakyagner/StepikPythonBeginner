import ifnumber
print("Сумма чисел 2")
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
    if i ** 2 % 10 == 2 or i ** 3 % 10 == 5 or i ** 3 % 10 == 8:
        total += 1

print(f"Количество чисел в диапазоне от 1 до {n} (включительно), квадрат которых оканчивается на 2, 5 или 8 = {total}.")

# Как объяснить пользователю, что это за число - n? Каким оно должно быть?
# В выводе знак = ставь только тогда, когда ты выводишь математическое выражение. В остальных случаях нужно писать "равно" словами