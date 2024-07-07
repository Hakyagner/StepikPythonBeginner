print("Количество чётных чисел")
print()

while True:
    num1 = input('Введи первое целое число: ')
    if num1.isdigit() or (num1[0] == "-" and num1[1:].isdigit()):
        break
    else:
        print("Нужно вести целое число")
        print()
while True:
    num2 = input('Введи второе целое число: ')
    if num2.isdigit() or (num2[0] == "-" and num2[1:].isdigit()):
        break
    else:
        print("Нужно вести целое число")
        print()
while True:
    num3 = input('Введи третье целое число: ')
    if num3.isdigit() or (num3[0] == "-" and num3[1:].isdigit()):
        break
    else:
        print("Нужно вести целое число")
        print()
even = 0
if int(num1) % 2 == 0:
    even += 1
if int(num2) % 2 == 0:
    even += 1
if int(num3) % 2 == 0:
    even += 1

print(f"Среди чисел {num1}, {num2} и {num3} есть {even} чётных чисел.")
