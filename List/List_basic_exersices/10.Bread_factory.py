events = input().split("|")

energy = 100
coins = 100
factory_is_open = True

for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    type_value = int(event_items[1])
    # here we are split rest-2 to rest type_of_event and type_of_value = 2
    if type_of_event == "rest":
        current_energy = energy
        energy += type_value
        if energy > 100:
            energy = 100
        gain_energy = energy - current_energy
        print(f"You gained {gain_energy} energy.")
        print(f'Current energy: {energy}.')
    elif type_of_event == 'order':
        if energy >= 30:
            energy -= 30
            coins += type_value
            print(f"You earned {type_value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins >= type_value:
            coins -= type_value
            print(f"You bought {type_of_event}.")
        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            factory_is_open = False
            break

if factory_is_open:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
