print("Церемония взвешивания")
print()

while True:
    weight = input('Введите ваш вес: ')
    if weight.isdigit() and int(weight) != 0:
        weight = int(weight)
        break
    else:
        print("Нужно ввести целое число")
if weight < 60:
    print(f"Боксёр с весом {weight} будет выступать в категодии 'Лёгкий вес'.")
elif weight < 64:
    print(f"Боксёр с весом {weight} будет выступать в категодии 'Первый полусредний вес'.")
else:
    print(f"Боксёр с весом {weight} будет выступать в категодии 'Полусредний вес'.")
