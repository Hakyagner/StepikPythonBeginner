print("Dog age")
print()

while True:
    dog_age = float("Введите возраст собаки: ")
    if dog_age > 0:
        break
    else:
        print("Возраст собаки должен быть больше 0.")
        print()

if 1 <= dog_age <= 2:
    print(f"Возрат собаки {dog_age} равен {dog_age * 10.5} годам по человечиским меркам.")
else:
    print(f"Возрат собаки {dog_age} равен {2 * 10.5 + (dog_age - 2) * 4} годам по человечиским меркам.")
