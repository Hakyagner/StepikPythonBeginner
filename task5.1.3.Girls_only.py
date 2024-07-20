print("Girls only")
print()

while True:
    year = input('Введите ваш возраст: ')
    if year.isdigit() and int(year) > 0:
        year = int(year)
        break
    else:
        print("Нужно ввести целое положительное число")
gender = input("Введите ваш пол - m (мужчина) или f (женщина): ")
if gender == "f" and 10 <= year <= 15:
    print(f"Поздравляем! Вы приняты в команду.")
else:
    print("К сожалению, вы не приняты в команду.")

# Ты говоришь, что нужно ввести f или m, но проверяешь и female
# Оптимизируй, чтобы принт вы не приняты в команду был только один раз
