print("Цветовой микшер")
print()

color1 = input("Введите название первого цвета: ")
color2 = input("Введите название второго цвета: ")

if color1.lower() != "красный" and color1.lower() != "синий" and color1.lower() != "жёлтый":
    print("Ошибка. Этот цвет не основной. Надо было ввести (красный или синий, или жёлтый)!")
elif color2.lower() != "красный" and color2.lower() != "синий" and color2.lower() != "жёлтый":
    print("Ошибка. Этот цвет не основной. Надо было ввести (красный или синий, или жёлтый)!")
elif color1.lower() == "красный" and color2.lower() == "синий":
    print(f"Из цветов {color1} и {color2} получается - фиолетовый")
elif color1.lower() == "синий" and color2.lower() == "красный":
    print(f"Из цветов {color1} и {color2} получается - фиолетовый")
elif (color1.lower() == "красный" and color2.lower() == "жёлтый") or (color2.lower() == "красный" and color1.lower() == "жёлтый"):
    print(f"Из цветов {color1} и {color2} получается - оранжевый")
elif (color1.lower() == "жёлтый" and color2.lower() == "синий") or (color2.lower() == "жёлтый" and color1.lower() == "синий"):
    print(f"Из цветов {color1} и {color2} получается - зелёный")
elif color1 == color2:
    print(f"Из цветов {color1} и {color2} получается - {color1}")

# Переделать с учетом функций для строк