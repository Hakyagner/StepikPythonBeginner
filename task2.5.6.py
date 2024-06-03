print("Номер купе")
print()
num = int(input("Введите номер своего места: "))
while True:
    num = input("Введите номер своего места: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
print((num - 1) // 4 + 1)
print()
