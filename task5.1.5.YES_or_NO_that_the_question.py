print("YES or NO вот в чем вопрос")
print()

while True:
    num = input('Введите целое положительное число: ')
    if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
        num = int(num)
        break
    else:
        print("Нужно ввести целое положительное число")
if num % 2 != 0 or 6 <= num <= 20:
    print('YES')
else:
    print('NO')

# Число какое должно быть???
