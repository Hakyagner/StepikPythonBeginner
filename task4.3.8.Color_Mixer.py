print("Цветовой микшер")
print()

color1 = input("Введите название первого цвета.")
color2 = input("Введите название второго цвета.")

if color1 != "красный" and color1 != "синий" and color1 != "жёлтый":
    print("Ошибка. Этот цвет не основно. Надо было ввести (красный или синий, или жёлтый)!")
elif color2 != "красный" and color2 != "синий" and color2 != "жёлтый":
    print("Ошибка. Этот цвет не основно. Надо было ввести (красный или синий, или жёлтый)!")
elif color1 == "красный" and color2 == "синий":
    print(f"Из цветов {color1} и {color2} получается - фиолетовый")
elif color1 == "синий" and color2 == "красный":
    print(f"Из цветов {color1} и {color2} получается - фиолетовый")
elif (color1 == "красный" and color2 == "жёлтый") or (color2 == "красный" and color1 == "жёлтый"):
    print(f"Из цветов {color1} и {color2} получается - оранжевый")
elif (color1 == "жёлтый" and color2 == "синий") or (color2 == "жёлтый" and color1 == "синий"):
    print(f"Из цветов {color1} и {color2} получается - зелёный")
elif color1 == color2:
    print(f"Из цветов {color1} и {color2} получается - {color1}")