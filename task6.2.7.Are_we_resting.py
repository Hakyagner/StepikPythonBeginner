print("Отдыхаем ли?")
print()

string = input("Введите любую строку: ")

if "суббота" in string or "воскресенье" in string:
    print(f"В строке {string} есть подстрока воскресенье или суббота.")
else:
    print(f"В строке {string} нет подстроки воскресенья или субботы.")