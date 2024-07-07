print("Обратное число")
print()

while True:
    num = input("Введите целое положительное число: ")
    if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
        num = int(num)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
if num == 0:
    print('Обратного числа не существует')
else:
    print(f"Обратное числу {num} - {1 / num}")
