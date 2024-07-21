import ifnumber
print("Первая цифра после точки")
print()

while True:
    num = input('Введи число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int':
        num = int(num)
        print()
        break
    elif if_number == 'float':
        num = float(num)
        break
    else:
        print('Данные введены некорректно! Нужно ввести число')
    print()

print(f"Первое число после точки равно {num * 10 % 10}.")

# Какое число нужно ввести?
# По выводу непонятно, откуда взялась первая цифра после точки
