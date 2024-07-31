import ifnumber
print("Обратное число")
print()

while True:
    num = input("Введите положительное число: ")
    if_number = ifnumber.if_number(num)
    if if_number == 'int':
        num = int(num)
        print()
        break
    if if_number == 'float':
        num = float(num)
        print()
        break
    else:
        print("Нужно ввести положительное число")
        print()

if num == 0:
    print('Обратного числа не существует')
else:
    print(f"Обратное числу {num} = {1 / num}.")

# done
