budget = float(input())
flour_price = float(input())
eggs_price = 0.75 * flour_price
milk_price = (1.25 * flour_price) / 4
colored_eggs = 0
for number_breads in range(1, int(budget) + 1):
    if eggs_price + milk_price + flour_price <= budget:
        budget -= (eggs_price + milk_price + flour_price)
        colored_eggs += 3
        if number_breads % 3 == 0:
            colored_eggs -= (number_breads - 2)
    else:
        print(
            f"You made {number_breads - 1} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
        break
# eggs = 0.9375
# milk = 0.390625
# 20.50
# 1.25
# 16 eggs are used and 7 loops you did for using easter bread. Every odd is taking 1 colored eggs
# You made 7 loaves of Easter bread! Now you have 16 eggs and 2.45BGN left.
# You made 5 loaves of Easter bread! Now you have 14 eggs and 1.31BGN left.
# 15.75
# 1.4
# Since it is Easter, you have decided to make some loaves of Easter bread and exchange them for eggs.
# Create a program that calculates how many loaves you can make (according to the recipe) with the budget you have.
# Here is the recipe for one loaf:
# Eggs	1 pack
# Flour	1 kg
# Milk	0.250 l
# First, you will receive your budget. Then, you will receive the price for 1 kg flour.
# The price for 1 pack of eggs is 75% of the price for 1 kg flour. The price for 1L milk is 25% more
# than the price for 1 kg flour. Keep in mind that you use only 250ml milk for a bread.
# Start cooking the loaves and keep making them until you have enough budget. Keep in mind that:
# •	For every loaf of bread that you make, you will receive 3 colored eggs.
# •	For every 3rd bread you make, you will lose some of your colored eggs after receiving the usual 3 colored
# eggs for your bread. The count of eggs you will lose is calculated when you subtract 2 from your current
# count of loaves - ({current_bread_count} - 2)
# In the end, print the loaves of bread you made, the eggs you have collected, and the money you
# have left, formatted to the 2nd decimal place, in the following format:
# "You made {number_of_loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {money_left}BGN left."
