number_of_snowballs = int(input())
weight_of_snowball = 0
time_target = 0
snowball_quality = 0
max_value = 0
for num in range(number_of_snowballs):
    current_weight = int(input())
    current_time = int(input())
    current_quality = int(input())
    current_value = (current_weight / current_time) ** current_quality
    if current_value > max_value:
        weight_of_snowball = current_weight
        time_target = current_time
        snowball_quality = current_quality
        max_value = current_value
print(f"{weight_of_snowball} : {time_target} = {int(max_value)} ({snowball_quality})")
# The weight of the snowball (integer).
# · The time needed for the snowball to get to its target (integer).
# · The quality of the snowball (integer).