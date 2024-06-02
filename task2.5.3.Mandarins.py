print("Мандарины")
print()
while True:
    Schoolchildren = input("Введите число школьников: ")
    if Schoolchildren.isdigit():
        Schoolchildren = int(Schoolchildren)
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
Schoolchildren_tangerines = tangerines // Schoolchildren
tangerines_tangerines = Schoolchildren * Schoolchildren_tangerines   # общее кол котор. был роздан кажд шк
Schoolchildren_Schoolchildren = tangerines - tangerines_tangerines
print("Достанется каждому школьнику по :", Schoolchildren_tangerines)
print("Количество оставшихся мандаринов :", Schoolchildren_Schoolchildren)
print()
