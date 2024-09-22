print("Количество членов")
print()

total = 0
while True:
    while True:
        text = input("Введи слово: ").lower().strip()
        if text == "":
            print("Строка не должна быть пустой!")
            print()
        elif " " in text:
            print("Нужно ввести одно слово.")
            print()
        else:
            break
    if text == "стоп" or text == "хватит" or text == "достаточно":
        break
    else:
        total += 1

print(f"Было введено {total} слов(а)")
