print("Красивое число")
print()

while True:
    num = input('Введи целое число: ')
    if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
        break
    else:
        print("Нужно ввести целое число")
        print()
if (num[0] == "-" and len(num) == 5) or len(num) == 4:
    if int(num) % 7 == 0 or int(num) % 17 == 0:
        print(f"Число {num} четырёхзначное и кратно 7 или 17")
    else:
        print(f"Число {num} четырёхзначное, но не кратно 7, или не кратно 17")
else:
    print(f"Число {num} не четырёхзначное.")
