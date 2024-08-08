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

maxsimum = max(len(city1), len(city2), len(city3))
minimum = min(len(city1), len(city2), len(city3))

if len(city1) == minimum:
    print(city1)
elif len(city2) == minimum:
    print(city2)
elif len(city3) == minimum:
    print(city3)

if len(city1) == maxsimum:
    print(city1)
elif len(city2) == maxsimum:
    print(city2)
elif len(city3) == maxsimum:
    print(city3)

# слишком много len. Избавься от них
