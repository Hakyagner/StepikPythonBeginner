import ifnumber
print("Dog age")
print()

while True:
    dog_age = input("Введите полный возраст собаки: ")
    if_number = ifnumber.if_number(dog_age)
    if if_number == 'int' and int(dog_age) > 0:
        dog_age = int(dog_age)
        print()
        break
    else:
        print("Нужно ввести целое положительное число.")
        print()

if 1 <= dog_age <= 2:
    print(f"Возраст собаки {dog_age} равен {dog_age * 10.5} человеческим годам.")
else:
    print(f"Возраст собаки {dog_age} равен {2 * 10.5 + (dog_age - 2) * 4} человеческим годам.")
