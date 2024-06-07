print("Номер купе")
print()
while True:
    num = input("Введите номер своего места: ")
    if num.isdigit() and 1 <= int(num) <= 36:
        num = int(num)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
print()
if num % 4 == 0:
    print(f"{num} место находится в {num // 4} купе")
else:
    print(f"{num} место находится в {num // 4 + 1} купе")
