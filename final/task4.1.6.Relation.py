print("Соотношение")
print()

while True:
    num = input('Введи целое положительное четырёхзначное число: ')
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Нужно вести целое положительное четырёхзначное число")
        print()
print()
num1 = (num // 100) // 10   # тысячи
num2 = (num // 100) % 10    # сотни
num3 = (num // 10) % 10     # десятки
num4 = num % 10     # единицы
total1 = num1 + num4
total2 = num2 - num3
if total1 == total2:
    print(f"{num1} + {num4} = {num2} - {num3}")
else:
    print(f"{num1} + {num4} != {num2} - {num3}")
