command = input()

foods_in_stock = {}
while command != 'statistics':
    foods = command.split(": ")
    name_of_product = foods[0]
    value_of_product = int(foods[1])
    if name_of_product not in foods_in_stock:
        foods_in_stock[name_of_product] = 0
    foods_in_stock[name_of_product] += value_of_product
    command = input()

print("Products in stock:")
for (name_of_product, value_of_product) in foods_in_stock.items():
    print(f"- {name_of_product}: {value_of_product}")
print(f"Total Products: {len(foods_in_stock.keys())}")
print(f"Total Quantity: {sum(foods_in_stock.values())}")
# input
# bread: 4
# cheese: 2
# ham: 1
# bread: 1
# statistics
# output
# Products in stock:
# - bread: 5
# - cheese: 2
# - ham: 1
# Total Products: 3
# Total Quantity:
