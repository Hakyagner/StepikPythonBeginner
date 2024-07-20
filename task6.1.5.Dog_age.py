import ifnumber
print("Dog age")
print()

while True:
    dog_age = input("Введите возраст собаки: ")
    if_number = ifnumber.if_number(dog_age)
    if if_number == 'int' and int(dog_age) > 0:
        dog_age = int(dog_age)
        print()
        break
    elif if_number == 'float' and int(dog_age) > 0:
        dog_age = float(dog_age)
        break
    else:
        print("Нужно ввести положительное число.")
        print()

if 1 <= dog_age <= 2:
    print(f"Возрат собаки {dog_age} равен {dog_age * 10.5} годам по человечиским меркам.")
else:
    print(f"Возрат собаки {dog_age} равен {2 * 10.5 + (dog_age - 2) * 4} годам по человечиским меркам.")

# Возраст - какое число?
# Русский язык