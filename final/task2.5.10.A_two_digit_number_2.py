print('Двузначное число 2')
print()
while True:
    ab = input('Введи целое положительное двузначное число: ')
    if ab.isdigit() and 10 <= int(ab) <= 99:
        ab = int(ab)
        break
    else:
        print("Нужно вести целое положительное двузначное число")
        print()
b = ab % 10
a = ab // 10
total = a + b
print(f"Сумма цифр числа {ab} равна {total}")
