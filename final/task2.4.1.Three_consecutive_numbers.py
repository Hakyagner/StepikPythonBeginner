print("Три последовательных числа")
print()

while True:
    num = input("Напиши число: ")
    if num.isdigit():
        num = int(num)
        print(num)
        print("Cледующее за числом", num, "-", num + 1)
        print("Cледующее за числом", num + 1, "-", num + 1 + 1)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
