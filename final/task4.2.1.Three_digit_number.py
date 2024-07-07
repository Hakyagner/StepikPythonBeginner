print("Трёхзначное число")
print()

while True:
    num = input('Введи целое положительное число: ')
    if num.isdigit():
        break
    else:
        print("Нужно вести целое положительное число")
        print()
print()
if len(num) == 3:
    print(f"Число {num} является трёхзначным числом")
else:
    print(f"Число {num} не является трёхзначным числом")
