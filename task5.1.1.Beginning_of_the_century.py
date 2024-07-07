print("Начало столетия")
print()

while True:
    year = input('Введи год: ')
    if year.isdigit() and int(year) > 0:
        break
    else:
        print("Нужно ввести целое положительное число")
if year[-1] and year[-2] == "0":
    print(f"{year} год является началом столетия.")
else:
    print(f"{year} год не является началом столетия.")
