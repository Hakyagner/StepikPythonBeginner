print("Цветовой микшер")
print()

color1 = input("Введите название первого цвета (красный, синий или жёлтый): ")
color2 = input("Введите название второго цвета (красный, синий или жёлтый): ")

if color1[1] == "e":
    color1[1] = "ё"
if color2[1] == "е":
    color2[1] = "ё"
if (color1.lower() != "красный" and color1.lower() != "синий" and color1.lower() != "жёлтый") or (color2.lower() != "красный" and color2.lower() != "синий" and color2.lower() != "жёлтый"):
    print("Ошибка! Я такого цвета не знаю.")
else:
    if color1.lower() == "красный" and color2.lower() == "синий":
        print(f"При смешивании цветов {color1} и {color2} получается - фиолетовый")
    elif (color1.lower() == "красный" and color2.lower() == "жёлтый") or (color2.lower() == "красный" and color1.lower() == "жёлтый"):
        print(f"При смешивании цветов {color1} и {color2} получается - оранжевый")
    elif (color1.lower() == "жёлтый" and color2.lower() == "синий") or (color2.lower() == "жёлтый" and color1.lower() == "синий"):
        print(f"При смешивании цветов {color1} и {color2} получается - зелёный")
    elif color1 == color2:
        print(f"При смешивании цветов {color1} и {color2} получается - {color1}")

# Не проходит 4 тест
