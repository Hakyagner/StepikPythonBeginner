print("Гонка спидстеров")
print()

while True:
    n = input('Введите скорость Зума: ')
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Нужно ввести целое положительное число")
while True:
    k = input('Введите скорость Флэша: ')
    if k.isdigit() or (k[0] == "-" and k[1:].isdigit()):
        k = int(k)
        break
    else:
        print("Нужно ввести целое положительное число")

if k > n:
    print(f"Прими вызов, ты сможешь выиграть!")
if k == n:
    print(f"Ваша скорость одинакова, поэтому лучше не рисковать.")
if k < n:
    print(f"Не принимай вызов, он быстрее тебя.")
