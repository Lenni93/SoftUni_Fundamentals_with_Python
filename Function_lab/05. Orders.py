def price_calculation(item,count):
    if item == "coffee":
        return count * 1.50
    if item == "water":
        return count * 1.00
    if item == "coke":
        return count * 1.40
    if item == "snacks":
        return count * 2.00

#coffee - 1.50
#water - 1.00
# coke - 1.40
#snacks - 2.00
product = input()
quality = int(input())
result = price_calculation(product,quality)
print(f'{result:.2f}')


# product = input()
# number_of_product = float(input())
# coffee = 1.50
# water = 1.00
# coke = 1.40
# snacks = 2.00
# total_price = 0
#
# if product == 'coffee':
#     total_price = number_of_product * coffee
# elif product == 'water':
#     total_price = number_of_product * water
# elif product == 'coke':
#     total_price = number_of_product * coke
# elif product == 'snacks':
#     total_price = number_of_product * snacks
#
# print(f'{total_price:.2f}')