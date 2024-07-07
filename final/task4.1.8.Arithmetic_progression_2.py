print("Арифметическая прогрессия 2")
print()

while True:
    num1 = input('Введи первое целое число: ')
    if num1.isdigit() or (num1[0] == "-" and num1[1:].isdigit()):
        num1 = int(num1)
        break
    else:
        print("Нужно вести целое число")
        print()
while True:
    num2 = input('Введи второе целое число: ')
    if num2.isdigit() or (num2[0] == "-" and num2[1:].isdigit()):
        num2 = int(num2)
        break
    else:
        print("Нужно вести целое число")
        print()
while True:
    num3 = input('Введи третье целое число: ')
    if num3.isdigit() or (num3[0] == "-" and num3[1:].isdigit()):
        num3 = int(num3)
        break
    else:
        print("Нужно вести целое число")
        print()
if num2 - num1 == num3 - num2:
    print(f"Последовательность чисел {num1}, {num2} и {num3} является арифметической прогрессией.")
else:
    print(f"Последовательность чисел {num1}, {num2} и {num3} не является арифметической прогрессией.")
