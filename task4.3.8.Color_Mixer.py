print("Цветовой микшер")
print()

color1 = input("Введите название первого цвета (красный, синий или жёлтый): ")
color2 = input("Введите название второго цвета (красный, синий или жёлтый): ")

color1 = color1.lower().replace("е", "ё")
color2 = color2.lower().replace("е", "ё")

if (color1 == "красный" or color1 == "синий" or color1 == "жёлтый") or (color2 == "красный" or color2 == "синий" or color2 == "жёлтый"):
    if color1 == "красный" and color2 == "синий":
        print(f"При смешивании цветов {color1} и {color2} получается - фиолетовый")
    elif (color1 == "красный" and color2 == "жёлтый") or (color2 == "красный" and color1 == "жёлтый"):
        print(f"При смешивании цветов {color1} и {color2} получается - оранжевый")
    elif (color1 == "жёлтый" and color2 == "синий") or (color2 == "жёлтый" and color1 == "синий"):
        print(f"При смешивании цветов {color1} и {color2} получается - зелёный")
    elif color1 == color2:
        print(f"При смешивании цветов {color1} и {color2} получается - {color1}")
else:
    print("Ошибка! Я такого цвета не знаю.")

# done
