monitor_price = int(input("Напишите стоимость монитора: "))
block_price = int(input("Напишите стоимость системного блока: "))
keyboard_price = int(input("Напишите стоимость клавиатуры: "))
mouse_price = int(input("Напишите стоимость мыши: "))
computer = monitor_price + block_price + keyboard_price + mouse_price
computer3 = computer + computer + computer
print("Стоимость 1 монитора:", monitor_price)
print("Стоимость 1 системного блока:", block_price)
print("Стоимость 1 клавиатуры:", keyboard_price)
print("Стоимость 1 мыши:", mouse_price)
print("Стоимость 3 компьютеров:", computer3)
