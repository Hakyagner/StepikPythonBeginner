print("Двузначное число")
print()
while True:
    num = input("Напиши двузначное целое положительное число: ")
    if num.isdigit() and 10 <= int(num) <= 99:
        num = int(num)
        break
    else:
        print("Нужно ввести двузначное целое положительное число")
        print()
tens = num // 10
units = num % 10
print()
print(f"Единицы числа {num} - это {units}")
print(f"Десятки числа {num} - это {tens}")
