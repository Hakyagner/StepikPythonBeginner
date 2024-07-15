print("Корректный email")
print()

email = input("Введите свой email адрес: ")

if '@' in email and '.' in email:
    print(f"Ваш email адрес {email} является корректен.")
else:
    print(f"Ваш email адрес {email} является не корректен.")
