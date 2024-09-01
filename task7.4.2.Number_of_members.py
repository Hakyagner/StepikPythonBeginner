print("Количество членов")
print()

sequence = ""
text = input("Введи строку:")
total = 0
while text.lower() != 'стоп' and text.lower() != 'хватит' and text.lower() != 'достаточно':
    total += 1
    sequence += (text + " ")
    text = input("Введи строку:")

print(f"Общее количество членов {sequence}последовательности {total}")
