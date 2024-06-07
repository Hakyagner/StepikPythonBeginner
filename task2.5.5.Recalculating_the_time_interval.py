print("Пересчёт временного интервала")
print()
while True:
    minutes1 = input("Введите количество минут: ")
    if minutes1.isdigit():
        minutes1 = int(minutes1)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
clock = minutes1 // 60
minutes2 = minutes1 % 60
print()
print(f"{minutes1} минут - это {clock} часов {minutes2} минут.")
