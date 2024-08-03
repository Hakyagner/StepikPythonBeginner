import ifnumber
print("Повторяй за мной 1")
print()

string = input("Введите строку: ")

while True:
    num = input('Введите сколько раз надо будет повторить вашу видённую строку: ')
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
print(num)

for i in range(num):
    print(num)

# done
