print("Арифметические строки")
print()

str1 = len(input("Введите первую строку: "))
str2 = len(input("Введите вторую строку: "))
str3 = len(input("Введите третью строку: "))

max_len = max(str1, str2, str3)
min_len = min(str1, str2, str3)
average_len = str1 + str2 + str3 - max_len - min_len

if average_len - min_len == max_len - average_len:
    print(f"Из длин этих строк - {str1}, {str2}, {str3} можно построить арифметическую прогрессию.")
else:
    print(f"Из длин этих строк - {str1}, {str2}, {str3} нельзя построить арифметическую прогрессию.")

# НЕПРАВИЛЬНО!!!
# проверять свои решения не пробовала????