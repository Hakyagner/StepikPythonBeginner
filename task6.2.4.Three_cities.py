print("Три города")
print()

while True:
    city1 = input("Введите название первого города: ")
    if len(city1) > 0:
        break
    else:
        print("Ошибка! Введите название города, у которога длина символов не равна 0. ")
while True:
    city2 = input("Введите название второго города: ")
    if len(city2) > 0:
        break
    else:
        print("Ошибка! Введите название города, у которога длина символов не равна 0. ")
while True:
    city3 = input("Введите название третьего города: ")
    if len(city3) > 0:
        break
    else:
        print("Ошибка! Введите название города, у которога длина символов не равна 0. ")
print()

maxsimum = max(len(city1), len(city2), len(city3))
minimum = min(len(city1), len(city2), len(city3))

print(f"Из названий трёх годов -  {city1, city2, city3} самое длиное название у города - {maxsimum} самое короткое название у города - {minimum}.")

# Неправильно
