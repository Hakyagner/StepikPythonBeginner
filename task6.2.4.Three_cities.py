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

city_1 = len(city1)
city_2 = len(city2)
city_3 = len(city3)

maxsimum = max(city_1, city_2, city_3)
minimum = min(city_1, city_2, city_3)

if city_1 == minimum:
    print(city1)
elif city_2 == minimum:
    print(city2)
elif city_3 == minimum:
    print(city3)

if city_1 == maxsimum:
    print(city1)
elif city_2 == maxsimum:
    print(city2)
elif city_3 == maxsimum:
    print(city3)

# done
