import ifnumber
print("Наименьший делитель")
print()

while True:
    n = input('Введи целое число больше 1: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 1:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число больше 1')
        print()

i = 2

while True:
    if n % i == 0:
        print(i)
        break
    i += 1
