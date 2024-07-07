print()
print()

while True:
    abc = input('Введи целое положительное трёхзначное число: ')
    if abc.isdigit() and 100 <= int(abc) <= 999:
        break
    else:
        print("Нужно вести целое положительное трёхзначное число")
        print()
print()
print(abc)
print(abc[2] + abc[1] + abc[0])
print(abc[0] + abc[2] + abc[1])
print(abc[2] + abc[0] + abc[1])
print(abc[1] + abc[0] + abc[2])
print(abc[1] + abc[2] + abc[0])
