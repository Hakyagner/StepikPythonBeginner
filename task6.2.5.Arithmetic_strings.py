print("Арифметические строки")
print()

str_len_1 = len(input("Введите первую строку: "))
str_len_2 = len(input("Введите вторую строку: "))
str_len_3 = len(input("Введите третью строку: "))

if abs(str_len_2 - str_len_1) == abs(str_len_3 - str_len_2) or abs(str_len_2 - str_len_3) == abs(str_len_3 - str_len_1) or abs(str_len_2 - str_len_1) == abs(str_len_3 - str_len_1):
    print(f"Из длин этих строк - {str_len_1}, {str_len_2}, {str_len_3} можно построить арифметическую прогрессию.")
else:
    print(f"Из длин этих строк - {str_len_1}, {str_len_2}, {str_len_3} нельзя построить арифметическую прогрессию.")

# из длин каких строк?
