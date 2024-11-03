import ifnumber

print("Упорядоченные цифры")
print()

while True:
    num = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
        print()

num1 = num
flag = True
last_digit = num % 10
num = num // 10

while num != 0:
    num2 = num % 10
    if last_digit > num2:
        flag = False
    last_digit = num2
    num = num // 10

ins = "не "
if flag:
    ins = ""
print(f"Последовательность цифр в числе {num1} при просмотре справа налево {ins}является упорядоченной по неубыванию.")
