print("Количество дней")
print()

while True:
    month = input('Введи номер месяца: ')
    if month.isdigit() and 13 > int(month) > 0:
        month = int(month)
        break
    else:
        print("Нужно ввести целое число от 1 до 13")

if month == 2:
    print(f"В месяце под номером {month} - 28 дней")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(f"В месяце под номером {month} - 30 дней")
else:
    print(f"В месяце под номером {month} - 31 день")
