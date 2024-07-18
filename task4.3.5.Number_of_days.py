print("Количество дней")
print()

while True:
    month = input('Введи номер месяца: ')
    if month.isdigit() or (month[0] == "-" and month[1:].isdigit()):
        month = int(month)
        break
    else:
        print("Нужно ввести целое число")

if month == 2:
    print(f"В месяце под номером {month} - 28 дней")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(f"В месяце под номером {month} - 30 дней")
else:
    print(f"В месяце под номером {month} - 31 день")

# Номер месяца может быть отрицательным???