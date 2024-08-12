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

# Если ты в input что-то спрашиваешь, не нужно писать "Введите". Только вопрос
# Русский язык
# Если ты просишь ввести число, ты ВСЕГДА должна понимать, каким это число должно быть
