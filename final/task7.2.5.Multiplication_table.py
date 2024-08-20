import ifnumber
print("Таблица умножения")
print()

while True:
    n = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(n)
    if if_number == 'int' and int(n) > 0:
        n = int(n)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
print()

for i in range(1, 11):
    total = n * i
    print(f"{n} x {i} = {total}")

# done
