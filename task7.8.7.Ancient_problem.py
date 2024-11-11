print("Старинная задача")
print()

max_bulls = 100 // 10
max_cows = 100 // 5

for bulls in range(max_bulls + 1):
    for cows in range(max_cows + 1):
        calves = 100 - (bulls + cows)
        if calves >= 0:
            if (bulls * 10 + cows * 5 + calves * 0.5) == 100:
                print(f"Быков = {bulls}, коров = {cows}, телят = {calves}")
