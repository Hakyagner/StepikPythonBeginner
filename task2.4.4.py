a = int(input("Напишите первое число: "))
b = int(input("Напишите второе число: "))
degree = (a + b) * (a + b) * (a + b)
summand1 = 3 * degree
summand2 = 275 * b * b
summand3 = 127 * a
print(summand1 + summand2 - summand3 - 41)
