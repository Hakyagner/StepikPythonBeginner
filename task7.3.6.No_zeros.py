import ifnumber
print("Без нулей")
print()

total = 1
for i in range(10):
    while True:
        num = input('Введи целое число: ')
        if_number = ifnumber.if_number(num)
        if if_number == 'int' or (num[0] == "-" and num[1:].isdigit()):
            num = int(num)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    if num != 0:
        total *= num

print(f"Произведение отличных от нуля чисел равно {total}")
