import ifnumber
print("Повторяй за мной 1")
print()

string = input("Введите строку: ")

while True:
    num = input('Сколько раз надо будет повторить вашу строку: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()
print()

for i in range(num):
    print(string)

# done
