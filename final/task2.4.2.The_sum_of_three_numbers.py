print("Сумма трёх чисел")
print()

while True:
    num1 = input("Напиши первое число: ")
    if num1.isdigit():
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    num2 = input("Напиши второе число: ")
    if num2.isdigit():
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    num3 = input("Напиши третье число: ")
    if num3.isdigit():
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
num4 = int(num1) + int(num2) + int(num3)
print()
print(f"{num1} + {num2} + {num3} = {num4}")

# Числа могут быть и отрицательными
