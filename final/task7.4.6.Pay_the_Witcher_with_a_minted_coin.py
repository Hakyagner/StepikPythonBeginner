import ifnumber
print("Ведьмаку заплатите чеканной монетой")
print()

while True:
    summa = input('Сколько нужно заплатить Ведьмаку? ')
    if_number = ifnumber.if_number(summa)
    if if_number == 'int' and int(summa) >= 0:
        summa = int(summa)
        break
    else:
        print('Данные введены некорректно! Нужно ввести целое число')
    print()
print()

total = 0

while summa != 0:
    if summa >= 25:
        summa -= 25
    elif 10 <= summa < 25:
        summa -= 10
    elif 5 <= summa < 10:
        summa -= 5
    else:
        summa -= 1
    total += 1

print(f"Ведьмаку нужно отдать минимум {total} чеканных монет.")
