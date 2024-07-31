import ifnumber
print("YES or NO вот в чем вопрос")
print()

while True:
    num = input('Введи целое положительное число: ')
    if_number = ifnumber.if_number(num)
    if if_number == 'int' and int(num) > 0:
        num = int(num)
        print()
        break
    elif if_number == 'float':
        num = float(num)
        print()
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое положительное число')
    print()

if num % 2 != 0 or (num % 2 == 0 and 6 <= num <= 20):
    print(f'Число {num} мне подходит')
elif (num % 2 == 0 and 2 <= num <= 5) or (num % 2 == 0 and num > 20):
    print(f'Число {num} мне не подходит')

# done
