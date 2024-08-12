print("Три города")
print()

while True:
    city1 = input("Введите название первого города: ")
    if len(city1) > 0:
        break
    else:
        print("Ошибка! Нужно ввести не пустую строку")
while True:
    city2 = input("Введите название второго города: ")
    if len(city2) > 0:
        break
    else:
        print("Ошибка! Нужно ввести не пустую строку")
while True:
    city3 = input("Введите название третьего города: ")
    if len(city3) > 0:
        break
    else:
        print("Ошибка! Нужно ввести не пустую строку")
print()

min_city = 0
max_city = 0

city_1 = len(city1)
city_2 = len(city2)
city_3 = len(city3)

maximum = max(city_1, city_2, city_3)
minimum = min(city_1, city_2, city_3)

if city_1 == minimum:
    min_city += city1
elif city_2 == minimum:
    min_city += city2
elif city_3 == minimum:
    min_city += city3

if city_1 == maximum:
    max_city += city1
elif city_2 == maximum:
    max_city += city2
elif city_3 == maximum:
    max_city += city3

print(f"Из трёх городов {city1}, {city2}, {city3} самое короткое название у города {min_city}")
print(f"Из трёх городов {city1}, {city2}, {city3} самое длинное название у города {max_city}")

# done
