print("Наименьшее из двух чисел")
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
print()
if num1 < num2:
    print(f"{num1} меньше, чем {num2}")
else:
    print(f"{num2} меньше, чем {num1}")
