element = input().split(" ")
products = {}
for i in range(0, len(element), 2):
    key = element[i]
    value = element[i + 1]
    products[key] = int(value)
search_element = input().split(" ")
for product in search_element:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
