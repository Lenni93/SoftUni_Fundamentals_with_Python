from math import floor


def center_point(sum1, sum2):
    if sum1 <= sum2:
        return f"({x1}, {x2})"
    elif sum1 >= sum2:
        return f"({y1}, {y2})"


x1 = floor(float(input()))
x2 = floor(float(input()))
y1 = floor(float(input()))
y2 = floor(float(input()))
sum_x = floor(abs(x1) + abs(x2))
sum_y = floor(abs(y1) + abs(y2))
print(center_point(sum_x, sum_y))

# sum of x1 is 24
# sum of x2 is 34
# so if 24 < from 34 is equal to (10, 14)
# if 34 is greater then 24 is equal to (18, 16)
# same here with input 2, 4 , -1 , 2
# output: (1, 2)

# You will be given the coordinates of two points on a
# Cartesian coordinate system - X1, Y1, X2, and Y2 on separate lines.
# Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in
# the format: "({X}, {Y})"
# If the points are at the same distance from the center, print only the first one. The resulting coordinates must be formatted to the lower integer.
