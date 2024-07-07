print("Одинаковые цифры")
print()

while True:
    num = input('Введи целое положительное двухзначное число: ')
    if num.isdigit() and 10 <= int(num) <= 99:
        break
    else:
        print("Нужно вести целое положительное двухзначное число")
        print()
if num[0] == num[1]:
    print(f"Число {num} состоит из одинаковых цифр")
else:
    print(f"Число {num} не состоит из одинаковых цифр")
