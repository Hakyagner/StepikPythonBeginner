print("Все разные")
print()

while True:
    num = input('Введи целое положительное трёхзначное число: ')
    if num.isdigit() and 100 < int(num) < 999:
        break
    else:
        print("Нужно ввести целое положительное трёхзначное число")
        print()
print()

if num[0] != num[1] and num[2] != num[1] and num[2] != num[0]:
    print(f"Все цифры числа {num} различны")
else:
    print(f"В числе {num} есть одинаковые цифры")
