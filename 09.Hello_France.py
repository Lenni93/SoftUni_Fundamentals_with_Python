items_accessories = input().split("|")
budget = int(input())

items_price, budget_left, train_ticket = 0, budget, 150

for clean_text in items_accessories:
    type_item, price = (float(x) if x[-1].isdigit() else x for x in clean_text.split('->'))
    if budget_left < price:
        continue
    if any(("Clothes" in type_item and price <= 50,
            "Shoes" in type_item and price <= 35,
            "Accessories" in type_item and price <= 20.50)):
        items_price += price
        budget_left -= price
        print(f'{price * 1.40:.2f}', end=" ")

difference = items_price * 1.4 - items_price
print(f"\nProfit: {difference:.2f}")

if budget + difference > train_ticket:
    print(f"Hello, France!")
else:
    print("Not enough money.")
