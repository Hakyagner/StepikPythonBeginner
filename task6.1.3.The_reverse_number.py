print("Обратное число")
print()

while True:
    num = input("Введите целое положительное число: ")
    if num.isdigit() and int(num) > 0:
        num = int(num)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()

if num == 0:
    print('Обратного числа не существует')
else:
    print(f"Обратное числу {num} = {1 / num}.")

# Читай внимательно условие задачи
