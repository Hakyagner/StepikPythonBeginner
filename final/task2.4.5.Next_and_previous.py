print("Следующее и предыдущее")
print()
while True:
    num = input("Напиши число: ")
    if num.isdigit():
        num = int(num)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
print("Следующее за числом", num, "число:", num + 1)
print("Для числа", num, "предыдущее число:", num - 1)
