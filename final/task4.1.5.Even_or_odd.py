print("Чётное или нечётное?")
print()

while True:
    num = input('Введи целое число: ')
    if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
        num = int(num)
        break
    else:
        print("Нужно вести целое число")
        print()
if num % 2 == 0:
    print(f"Число {num} чётное")
else:
    print(f"Число {num} не чётное")
