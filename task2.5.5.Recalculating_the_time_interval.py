print("Пересчёт временного интервала")
print()
while True:
    Minutes1 = input("Введите количество минут: ")
    if Minutes1.isdigit():
        Minutes1 = int(Minutes1)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
clock = Minutes1 // 60
Minutes2 = Minutes1 % 60
print()
print(Minutes1, "мин", "- это", clock, "час", Minutes2, "минут.")

# названия переменных начинаются с маленькой буквы