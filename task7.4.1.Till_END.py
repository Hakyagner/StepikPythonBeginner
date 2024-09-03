print("До КОНЦА")
print()

sequence = ""
text = input("Введи строку:")
while text.upper() != 'КОНЕЦ':
    sequence += (text + " ")
    print(f"Члены {sequence}последовательности равны {text}")
    text = input("Введи строку:")

# Введи пустую строку
