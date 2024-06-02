print("Следующее и предыдущее")
print()
while True:
    monitor_price = input("Напишите стоимость монитора: ")
    if monitor_price.isdigit():
        monitor_price = int(monitor_price)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    block_price = input("Напишите стоимость системного блока: ")
    if block_price.isdigit():
        block_price = int(block_price)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    keyboard_price = input("Напишите стоимость клавиатуры: ")
    if keyboard_price.isdigit():
        keyboard_price = int(keyboard_price)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
while True:
    mouse_price = input("Напишите стоимость мыши: ")
    if mouse_price.isdigit():
        mouse_price = int(mouse_price)
        break
    else:
        print("Нужно ввести целое положительное число")
        print()
computer = monitor_price + block_price + keyboard_price + mouse_price
computer3 = computer + computer + computer
print("Стоимость 1 монитора:", monitor_price)
print("Стоимость 1 системного блока:", block_price)
print("Стоимость 1 клавиатуры:", keyboard_price)
print("Стоимость 1 мыши:", mouse_price)
print("Стоимость 3 компьютеров:", computer3)

# Переменные не определены до цикла