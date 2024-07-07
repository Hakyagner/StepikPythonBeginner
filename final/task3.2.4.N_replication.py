print("Размножение n-ок")
print()

while True:
    n = input('Введи целое число от 1 до 9: ')
    if n.isdigit() and 0 < int(n) <= 9:
        n = int(n)
        break
    else:
        print("Нужно вести целое число от 1 до 9")
        print()
print()
nn = n * 10 + n
nnn = nn * 10 + n
total = n + nn + nnn
print(total)
