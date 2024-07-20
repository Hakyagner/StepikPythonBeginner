import ifnumber
print("Наибольшие числа")
print()

while True:
    n = input('Введи число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        print()
        break
    elif if_number == 'float' and int(n) > 0:
        n = float(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести положительное число')
    print()

maxsimum1 = 0
maxsimum2 = 0

for i in range(n):
    n_n = int(input("Введите число: "))
    if n_n > maxsimum1:
        maxsimum1 = n_n
        maxsimum2 = maxsimum1
    elif n_n > maxsimum2:
        maxsimum2 = n_n

print(f"{maxsimum1}")
print(f"{maxsimum2}")
