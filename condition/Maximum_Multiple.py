divisor = int(input())
boundary = int(input())
target = 0
for number in range(1, boundary + 1):
    number_check = number / divisor
    if 0 < number <= boundary and number_check.is_integer():
        target = number

print(target)

# when is 2 we got target to every 2 as example 2,7 we have in the loops 2,4,6and we print the last largest number
# with divisor we decide with which one we will divisor so we divisor on by 2
# next one is with 10, 50 we divide every 10. so we have fist 10 then 20,30,40 till 50 and the last one is 50

# On the first line, you will be given a positive number, which will serve as a divisor.
# On the second line, you will receive a positive number that will be the boundary.
# You should find the largest integer N, that is:
# •	divisible by the given divisor
# •	less than or equal to the given bound
# •	greater than 0
# Note:it is guaranteed that N is found.