print("Арифметические строки")
print()

str1 = len(input("Введите первую сторку: "))
str2 = len(input("Введите вторую строку: "))
str3 = len(input("Введите третью строку: "))

if str1 - str2 == str2 - str3 or str1 - str3 == str3 - str2 or str2 - str1 == str1 - str3:
    print(f"Из длин строк - {str1, str2, str3} можно построить арифметическую прогрессию.")
else:
    print(f"Из длин строк - {str1, str2, str3} нельзя построить арифметическую прогрессию.")

# Неправильно