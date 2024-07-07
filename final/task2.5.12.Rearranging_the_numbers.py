print('Перестановка цифр')
print()

while True:
    ab = input('Введи целое положительное двузначное число: ')
    if ab.isdigit() and 10 <= int(ab) <= 99:
        break
    else:
        print("Нужно вести целое положительное двузначное число")
        print()
print()
ba = ab[1] + ab[0]
print(f"После перестановки цифр в числе {ab} получается число {ba}")
