print("Гипотеза Эйлера о сумме степеней")
print()

limit = 150

for a in range(1, limit + 1):
    for b in range(a, limit + 1):
        for c in range(b, limit + 1):
            for d in range(c, limit + 1):
                summa_stepeney = a ** 5 + b ** 5 + c ** 5 + d ** 5
                e = int(summa_stepeney ** (1 / 5))    # a5 + b5 + c5 + d5 = e5.
                if summa_stepeney == e ** 5:
                    print(f"{a} ** 5 + {b} ** 5 + {c} ** 5 + {d} ** 5 = {e} ** 5 = {e ** 5}")
                    print(f"Сумма чисел a, b, c, d, e равна {a + b + c + d + e}")
                    break
