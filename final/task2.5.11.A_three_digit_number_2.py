print('Трёхзначное число 2')
print()
while True:
    abc = input('Введи целое положительное трёхзначное число: ')
    if abc.isdigit() and 100 <= int(abc) <= 999:
        abc = int(abc)
        break
    else:
        print("Нужно вести целое положительное трёхзначное число")
        print()
c = abc % 10
b = (abc // 10) % 10
a = abc // 100
total = a + b + c
mult = a * b * c
print(f"Сумма цифр числа {abc} равна {total}")
print(f"Произведение цифр числа {abc} равно {mult}")
