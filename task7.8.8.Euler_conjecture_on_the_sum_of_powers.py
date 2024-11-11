print("Гипотеза Эйлера о сумме степеней")
print()

limit = 150

for a in range(1, limit + 1):
    for b in range(a, limit + 1):
        for c in range(b, limit + 1):
            for d in range(c, limit + 1):
                e = int((a ** 5 + b ** 5 + c ** 5 + d ** 5) ** (1 / 5))    # a5 + b5 + c5 + d5 = e5.
                if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                    print(f"Найденные числа: a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")
                    print(f"Сумма чисел a, b, c, d, e равна {a + b + c + d + e}")
                    break
