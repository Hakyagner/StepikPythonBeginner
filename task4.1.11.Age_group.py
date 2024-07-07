print("Возрастная группа")
print()

while True:
    years = input('Введите ваш возраст: ')
    if years.isdigit() and 1 <= int(years):
        years = int(years)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
print()
if years <= 13:
    print("Вы относитесь к возрастной группе: детство")
elif 14 <= years <= 24:
    print("Вы относитесь к возрастной группе: молодость")
elif 25 <= years <= 59:
    print("Вы относитесь к возрастной группе: зрелость")
else:
    print("Вы относитесь к возрастной группе: старость")
