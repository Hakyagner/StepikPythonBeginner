print("YES or NO вот в чем вопрос")
print()

while True:
    num = input('Введите целое число: ')
    if num.isdigit() or (num[0] == "-" and num[1:].isdigit()):
        num = int(num)
        break
    else:
        print("Нужно ввести целое число")
if num % 2 != 0:
    print("YES")
elif num % 2 == 0 and 2 <= num <= 5:
    print("NO")
elif num % 2 == 0 and 6 <= num <= 20:
    print("YES")
elif num % 2 == 0 and num > 20:
    print("NO")
else:
    print(f"Ошибка. Число {num} не соответствует ни одному из требований.")

# Оптимизируй вывод
