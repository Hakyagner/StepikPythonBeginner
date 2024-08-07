import ifnumber

print("Интересное число")
print()

while True:
    abc = input('Введи целое положительное трёхзначное число: ')
    if_number = ifnumber.if_number(abc)
    if if_number == 'int' and 100 <= int(abc) <= 999:
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное трёхзначное число')
    print()

num1 = int(abc[0])
num2 = int(abc[1])
num3 = int(abc[2])

maximum = max(num1, num2, num3)
minimum = min(num1, num2, num3)

total1 = maximum - minimum

total2 = num1 + num2 + num3
average = total2 - maximum - minimum

if total1 == average:
    print(f"У Числа {abc} разность максимальной и минимальной цифр равняется средней по величине цифре.")
else:
    print(f"У Числа {abc} разность максимальной и минимальной цифр не равняется средней по величине цифре.")

# done
