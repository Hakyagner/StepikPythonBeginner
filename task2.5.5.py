Minutes1 = int(input("Введите количество минут: "))
clock = Minutes1 // 60
Minutes2 = Minutes1 % 60
print(Minutes1, "мин", "- это", clock, "час", Minutes2, "минут.")
