print("Цвета колеса рулетки")
print()

while True:
    number = input('Введи номер кармана: ')
    if number.isdigit() or (number[0] == "-" and number[1:].isdigit()):
        number = int(number)
        break
    else:
        print("Нужно ввести целое число")
if 0 > number or 36 < number:
    print(f"Ошибка. Число {number} не лежит в диапазоне (от 0 до 36).")
elif 1 <= number <= 10 or 19 <= number <= 28:
    if number % 2 == 0:
        print(f"Карман с номером {number} является чёрным.")
    else:
        print(f"Карман с номером {number} является красным.")
elif 11 <= number <= 18 or 29 <= number <= 36:
    if number % 2 == 0:
        print(f"Карман с номером {number} является красным.")
    else:
        print(f"Карман с номером {number} является чёрным.")
elif number == 0:
    print(f"Карман с номером {number} является зелёным.")
