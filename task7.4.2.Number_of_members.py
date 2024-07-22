print("Количество членов")
print()

textst = input("Введите текст: ")

total = 0

while textst.lower() != 'стоп' or textst.lower() != 'хватит' and textst.lower() != 'достаточно':
    total += 1
    print(total)
    textst = input("Введите текст: ")
