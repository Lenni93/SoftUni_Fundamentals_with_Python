group_number = int(input())
day_of_adventure = int(input())
coins = 0
for current_day in range(1, day_of_adventure + 1):
    if current_day % 10 == 0:
        group_number -= 2
    if current_day % 15 == 0:
        group_number += 5
    if current_day % 3 == 0:
        coins -= group_number * 3
    if current_day % 5 == 0:
        coins += group_number * 20
        if current_day % 3 == 0:
            coins -= group_number * 2
    coins += 50
    coins -= group_number * 2
coins_per_companions = coins // group_number
print(f"{group_number} companions received {coins_per_companions} coins each.")