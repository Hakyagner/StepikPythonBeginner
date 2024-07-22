print("Only even numbers")
print()

total = 0

for i in range(10):
    n = int(input("Введите число: "))
    if n % 2 == 0:
        total += 1
if total == 10:
    print('Все числа чётные.')
else:
    print('Все числа не чётные.')
