print("Наименьшее из четырёх чисел")
print()

while True:
    num = input('Введи целое число: ')
    if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
        num = int(num)
        break
    else:
        print("Нужно вести целое число")
        print()
print()
num_min = num
for i in range(3):
    while True:
        num = input('Введи целое число: ')
        if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
            num = int(num)
            break
        else:
            print("Нужно вести целое число")
            print()
    if num_min > num:
        num_min = num
print(f"Минимальное из введённых чисел - {num_min}")
