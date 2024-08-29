import ifnumber
print("Без нулей")
print()

total = 1
for i in range(10):
    while True:
        if i == 0:
            num = input('Введи первое число: ')
        else:
            num = input('Введи следующее число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int':
            num = int(num)
            break
        elif if_number == 'float':
            num = float(num)
            break
        else:
            print('Данные введены некорректно! Нужно ввести число')
        print()
    if num != 0:
        total *= num

print(f"Произведение отличных от нуля чисел равно {total}")

# done
