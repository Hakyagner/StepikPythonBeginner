print("До КОНЦА")
print()

sequence = ""

while True:
    while True:
        text = input("Введи строку: ")
        if text == "":
            print(f"Строка не должна быть пустой.")
        else:
            break
    if text.upper() == 'КОНЕЦ':
        break
    print(text)

# done

