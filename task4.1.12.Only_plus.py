print("Только +")
print()

while True:
    num1 = input('Введи первое целое число: ')
    if num1.isdigit() or (num1[0] == "-" and num1[1:].isdigit()):
        num1 = int(num1)
        break
    else:
        print("Нужно ввести целое число")
        print()
while True:
    num2 = input('Введи второе целое число: ')
    if num2.isdigit() or (num2[0] == "-" and num2[1:].isdigit()):
        num2 = int(num2)
        break
    else:
        print("Нужно ввести целое число")
        print()
while True:
    num3 = input('Введи третье целое число: ')
    if num3.isdigit() or (num3[0] == "-" and num3[1:].isdigit()):
        num3 = int(num3)
        break
    else:
        print("Нужно ввести целое число")
        print()
print()
total = 0
if num1 > 0:
    total += num1
if num2 > 0:
    total += num2
if num3 > 0:
    total += num3

print(f"Cреди чисел {num1}, {num2} и {num3} сумма положительных чисел равна {total}")
