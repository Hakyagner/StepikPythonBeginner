print("Самописный калькулятор")
print()

while True:
    num1 = input('Введи первое целое число: ')
    if num1.isdigit() or (num1[0] == "-" and num1[1:].isdigit()):
        num1 = int(num1)
        break
    else:
        print("Нужно ввести целое число")
while True:
    num2 = input('Введи второе целое число: ')
    if num2.isdigit() or (num2[0] == "-" and num2[1:].isdigit()):
        num2 = int(num2)
        break
    else:
        print("Нужно ввести целое число")

total = 0
character = input('Введи знак операции (+, -, *, /): ')
if character == "-":
    print(f"{num1} {character} {num2} = {num1 - num2}")
elif character == "+":
    print(f"{num1} {character} {num2} = {num1 + num2}")
elif character == "*":
    print(f"{num1} {character} {num2} = {num1 * num2}")
elif character == "/":
    if num2 == 0:
        print("На нуль делить нельзя!")
    else:
        print(f"{num1} {character} {num2} = {num1 / num2}")
else:
    print("Неверная операция")
