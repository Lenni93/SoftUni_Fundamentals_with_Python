fist_order = int(input())

total = 0

for _ in range(fist_order):
    order = float(input())
    days = int(input())
    count_capsul = int(input())
    single_order = order * days * count_capsul
    if 0.01 <= order <= 100.00 and 1 <= days <= 31 and 1 <= count_capsul <= 2000:
        total += single_order
        print(f"The price for the coffee is: ${single_order:.2f}")

print(f"Total: ${total:.2f}")
# the first is order which is one by 1.53 for 30 days and 8 capsuls = 367.2
#  the second is 2 orders, 1st is by 4.99 *3 orders * 31 days = 464.07 + 2nd order by 0.35 *
#  3 capsuls * 31 days = 54 + 464.07 = 518.32
# You work at a coffee shop, and your job is to place orders to the distributors.
# Thus, you want to know the price of each order. On the first line,
# you will receive integer N - the number of orders the shop will receive. For each order,
# you will receive the following information:
# •	Price per capsule - a floating-point number in the range [0.01…100.00]
# •	Days - integer in the range [1…31]
# •	Capsules, needed per day - integer in the range [1…2000]
# For each order, you should print a single line in the following format:
# •	"The price for the coffee is: ${price}"
# If you do not receive a correct order (one or more of the values are not in the given range),
# you should ignore it and move to the next one.
# After you go through all orders, you need to print the total price in the following format:
# •	 "Total: ${total_price}"
# Both the price of a coffee and the total price must be formatted to the second decimal place.
#