car_races = input().split(' ')
timer_integer = []

for race in car_races:
    timer_integer.append(int(race))
middle_timer = len(timer_integer) // 2
left_side = timer_integer[0:middle_timer]
right_side = timer_integer[middle_timer + 1:][::-1]

left_time = 0
right_time = 0
for second_left_racer in left_side:
    left_time += second_left_racer
    if second_left_racer == 0:
        left_time -= 0.2 * left_time
for second_right_racer in right_side:
    right_time += second_right_racer
    if second_right_racer == 0:
        right_time -= 0.2 * right_time

if left_time > right_time:
    print(f"The winner is right with total time: {right_time:.1f}")
else:
    print(f"The winner is left with total time: {left_time:.1f}")
