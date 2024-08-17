print("Арифметические строки")
print()
str_1 = input("Введите первую строку: ")
str_2 = input("Введите вторую строку: ")
str_3 = input("Введите третью строку: ")
str_len_1 = len(str_1)
str_len_2 = len(str_2)
str_len_3 = len(str_3)

if abs(str_len_2 - str_len_1) == abs(str_len_3 - str_len_2) or abs(str_len_2 - str_len_3) == abs(str_len_3 - str_len_1) or abs(str_len_2 - str_len_1) == abs(str_len_3 - str_len_1):
    ins = "можно"
else:
    ins = "нельзя"
msg = f"Из длин этих строк - <{str_1}>, <{str_2}>, <{str_3}> {ins} построить арифметическую прогрессию."
print(msg)
# done
