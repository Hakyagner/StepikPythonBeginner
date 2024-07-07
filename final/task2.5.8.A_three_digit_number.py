print("Трёхзначное число")
print()

while True:
    abc = input('Введи целое положительное трёхзначное число: ')
    if abc.isdigit() and 100 <= int(abc) <= 999:
        break
    else:
        print("Нужно вести целое положительное трёхзначное число")
        print()
print()
print(f"Число {abc} состоит из цифр {abc[0]}, {abc[1]}, {abc[2]}")
