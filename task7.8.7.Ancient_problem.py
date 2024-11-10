
print("Старинная задача")
print()

for bulls in range(11):
    for cows in range(21):
        calves = 100 - (bulls + cows)
        if calves >= 0:
            if (bulls * 10 + cows * 5 + calves * 0.5) == 100:
                print(f"Быки = {bulls}, коровы = {cows}, телята = {calves}")
