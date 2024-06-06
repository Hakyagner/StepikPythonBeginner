print("Мандарины")
print()
while True:
    schoolchildren = input("Введите число школьников: ")
    if schoolchildren.isdigit() and schoolchildren != 0:
        schoolchildren = int(schoolchildren)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    tangerines = input("Введите число мандаринов: ")
    if tangerines.isdigit():
        tangerines = int(tangerines)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
print()
schoolchildren_tangerines = tangerines // schoolchildren
schoolchildren_schoolchildren = tangerines % schoolchildren
print("Достанется каждому школьнику по:", schoolchildren_tangerines, "мандаринов")
print("Количество оставшихся мандаринов в корзине:", schoolchildren_schoolchildren)
