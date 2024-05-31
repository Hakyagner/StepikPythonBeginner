population = int(input("Введите сколько людей на земле: "))
if population % 2 == 0:
    print("Жителей останется на земле :", int(population / 2))
else:
    print("Жителей останется на земле :", int((population / 2) + 1))
