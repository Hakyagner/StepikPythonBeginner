print("Расстояние в метрах")
print()
while True:
    num_centimetrs = input("Введите число: ")
    if num_centimetrs.isdigit():
        num_centimetrs = int(num_centimetrs)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
num_metr = num_centimetrs / 100
print()
print(f"{num_centimetrs} сантиметра = {num_metr} метра")

# Что нужно ввести?