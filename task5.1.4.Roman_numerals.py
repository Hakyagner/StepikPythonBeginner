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
elif num == 4:
    print(f"Римская цифра числа {num} - IV")
elif num < 9:
    print(f"Римская цифра числа {num} - {'V' + (num - 5) * 'I'}")
elif num < 11:
    print(f"Римская цифра числа {num} - {(10 - num) * 'I' + 'X'}")
else:
    print("Ошибка! Число не находится в диапазоне от 1 до 10.")

# done
