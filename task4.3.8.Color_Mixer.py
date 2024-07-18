print("Цветовой микшер")
print()

color1 = input("Введите название первого цвета: ")
color2 = input("Введите название второго цвета: ")

if (color1 != "красный" and color1 != "синий" and color1 != "жёлтый") or (color1 != "Красный" and color1 != "Синий" and color1 != "Жёлтый"):
    print("Ошибка. Этот цвет не основной. Надо было ввести (красный или синий, или жёлтый)!")
elif (color2 != "красный" and color2 != "синий" and color2 != "жёлтый") or (color2 != "Красный" and color2 != "Синий" and color2 != "Жёлтый"):
    print("Ошибка. Этот цвет не основной. Надо было ввести (красный или синий, или жёлтый)!")
elif (color1 == "красный" or color1 == "Красный") and (color2 == "синий" or color2 == "Cиний"):
    print(f"Из цветов {color1} и {color2} получается - фиолетовый")
elif (color1 == "синий" or color1 == "Cиний") and (color2 == "красный" or color2 == "Красный"):
    print(f"Из цветов {color1} и {color2} получается - фиолетовый")
elif ((color1 == "красный" or color1 == "Красный") and (color2 == "жёлтый" or color2 == "Жёлтый")) or ((color2 == "красный" or color2 == "Красный") and (color1 == "жёлтый" or color1 == "Жёлтый")):
    print(f"Из цветов {color1} и {color2} получается - оранжевый")
elif ((color1 == "жёлтый" or color1 == "Жёлтый") and (color2 == "синий" or color2 == "Синий")) or ((color2 == "жёлтый" or color2 == "Жёлтый") and (color1 == "синий" or color1 == "Синий")):
    print(f"Из цветов {color1} и {color2} получается - зелёный")
elif color1 == color2:
    print(f"Из цветов {color1} и {color2} получается - {color1}")
