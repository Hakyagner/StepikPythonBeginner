import ifnumber
print("Последовательность символов")
print()

while True:
    n = input('Введи ширину прямоугольника: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
print()

for i in range(n):
    print("*" * 19)

# done
