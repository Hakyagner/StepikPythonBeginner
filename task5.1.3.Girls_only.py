print("Girls only")
print()

while True:
    year = input('Введите ваш возраст: ')
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break
    else:
        print("Нужно ввести целое положительное число")
gender = input("Введите ваш пол используя обозначение пола буквы m (от male – мужчина) и f (от female – женщина):")
if gender == "f" or gender == "female":
    if 10 <= year <= 15:
        print(f"Поздравляем! Вы приняты в команду.")
    else:
        print("К сожалению, вы не приняты в команду.")
else:
    print("К сожалению, вы не приняты в команду.")
