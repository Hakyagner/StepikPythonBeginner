print("12 месяцев")
print()

for n in range(1, 13):
    for k in range(1, 13):
        for m in range(1, 13):
            if n + k + m > 12 or 28 * n + 30 * k + 31 * m > 365:
                break
            elif 28 * n + 30 * k + 31 * m == 365:
                print(f"28 * {n} + 30 * {k} + 31 * {m} = 365")
