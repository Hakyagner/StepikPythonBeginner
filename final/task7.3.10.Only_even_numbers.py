import ifnumber
print("Only even numbers")
print()

sequence = ""
counter = 0
for i in range(10):
    while True:
        n = input(f'Введи целое число {i + 1}: ')
        if_number = ifnumber.if_number(n)
        if if_number == 'int':
            sequence += (n + " ")
            n = int(n)
            break
        else:
            print('Данные введены некорректно! Нужно ввести целое число')
        print()
    if n % 2 == 0:
        counter += 1
if counter == 10:
    temp = ""
else:
    temp = "не"
print(f"В последовательности {sequence}{temp} все числа чётные")
