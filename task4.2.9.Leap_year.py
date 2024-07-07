print("Високосный год")
print()

while True:
    year = input('Введи год: ')
    if year.isdigit() and year != 0:
        year = int(year)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()

if year % 4 == 0 and year != 100 or year % 400 == 0:
    print(f"{year} год яляется високосным")
else:
    print(f"{year} год не яляется високосным")
