print("Арифметические операции")
print()
while True:
    num1 = input("Введите первое число: ")
    if num1.isdigit():
        num1 = int(num1)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    num2 = input("Введите второе число: ")
    if num2.isdigit():
        num2 = int(num2)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
num3 = num1 + num2
num4 = num1 - num2
num5 = num1 * num2
print()
print(num1, "+", num2, "=", num3)
print(num1, "-", num2, "=", num4)
print(num1, "*", num2, "=", num5)