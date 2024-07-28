print("Римские цифры")
print()

while True:
    num = input('Введите целое число от 1 до 10: ')
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Нужно ввести целое число от 1 до 10")
if 1 <= num <= 3:
    print(f"Римская цифра числа {num} - {num * "I"}")
elif 6 <= num <= 8:
    if num == 6:
        print(f"Римская цифра числа {num} - {"V" + "I"}")
    if num == 7:
        print(f"Римская цифра числа {num} - {"V" + "II"}")
    elif num == 8:
        print(f"Римская цифра числа {num} - {"V" + "III"}")
elif 9 <= num <= 10:
    if num == 9:
        print(f"Римская цифра числа {num} - {"I" + "X"}")
    else:
        print(f"Римская цифра числа {num} - X")
elif num == 5 or num == 4:
    if num == 5:
        print(f"Римская цифра числа {num} - V")
    else:
        print(f"Римская цифра числа {num} - {"I" + "V"}")
else:
    print("Ошибка! Число не находится в диапазоне от 1 до 10.")

# твои if в elif делают бессмысленными elif. Оптимизируй
