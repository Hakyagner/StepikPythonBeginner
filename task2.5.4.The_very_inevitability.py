print("Сама неотвратимость")
print()
while True:
    population = input("Введите сколько людей на земле: ")
    if population.isdigit():
        population = int(population)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
print()
if population % 2 == 0:
    print("Жителей останется на земле :", population // 2)
else:
    print("Жителей останется на земле :", (population // 2) + 1)
