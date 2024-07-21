print("Корректный email")
print()

email = input("Введите свой email адрес: ")

if '@' in email and '.' in email:
    print(f"Вы ввели корректный email адрес.")
else:
    print(f"Вы ввели некорректный email адрес.")
