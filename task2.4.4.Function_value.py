print("Значение функции")
print()
while True:
    a = input("Напишите первое число: ")
    if a.isdigit():
        a = int(a)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    b = input("Напишите второе число: ")
    if b.isdigit():
        b = int(b)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
degree = (a + b) * (a + b) * (a + b)
summand1 = 3 * degree
summand2 = 275 * b * b
summand3 = 127 * a
print(summand1 + summand2 - summand3 - 41)

# a и b до цикла не определены.
