# number_of_lines = int(input())
# water_counter = 0
# tank_capacity = 255
# for line in range(number_of_lines):
#     litters = int(input())
#     if tank_capacity - litters < 0:
#         print("Insufficient capacity!")
#         continue
#     tank_capacity -= litters
# print(255 - tank_capacity)
# # 255
number_of_lines = int(input())
water_counter = 0
tank_capacity = 255
for line in range(number_of_lines):
    litters = int(input())
    if tank_capacity - litters < 0:
        print("Insufficient capacity!")
        continue
    tank_capacity -= litters
    water_counter += litters
print(water_counter)
