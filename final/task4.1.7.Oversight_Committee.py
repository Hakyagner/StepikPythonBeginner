print("Роскомнадзор")
print()

while True:
    years = input('Введите ваш возраст: ')
    if years.isdigit():
        years = int(years)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
print()
if years < 18:
    print("Извините, вам доступ запрещен")
else:
    print("Доступ разрешен")
