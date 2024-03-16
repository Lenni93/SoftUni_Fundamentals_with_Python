given_items = []

while True:
    try:
        original_list = input().split()
        [given_items.append([original_list[i], original_list[i + 1].lower()]) for i in range(0, len(original_list), 2)]
    except:
        break

collected_items = {
        'shards': 0,
        'fragments': 0,
        'motes': 0
}
collected_item_name = {
    'shards': 'Shadowmourne',
    'fragments': 'Valanyr',
    'motes': 'Dragonwrath'
}

for quantity, item in given_items:
    collected_items[item] = collected_items.get(item, 0) + int(quantity)

    if item in collected_item_name:
        found = False

        for collected_item, collected_quantity in list(collected_items.items())[:3]:
            if collected_quantity >= 250:
                collected_items[collected_item] -= 250
                print(f"{collected_item_name[collected_item]} obtained!")
                found = True
                break

        if found:
            break

for item, quantity in collected_items.items():
        print(f"{item}: {quantity}")
