print("Цветовой микшер")
print()

color3 = input("Введите название первого цвета (красный, синий или жёлтый): ")
color4 = input("Введите название второго цвета (красный, синий или жёлтый): ")

color1 = color3.replace("e", "ё")
color2 = color4.replace("e", "ё")

if (color1.lower() != "красный" or color1.lower() != "синий" or color1.lower() != "жёлтый") or (color2.lower() != "красный" or color2.lower() != "синий" or color2.lower() != "жёлтый"):
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
