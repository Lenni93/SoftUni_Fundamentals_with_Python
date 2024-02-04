number = int(input())


def if_number_is_perfect(n):
    check_number = 0
    for i in range(1, n):
        if n % i == 0:
            check_number = check_number + i
    if check_number == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


print(if_number_is_perfect(number))
#   · "We have a perfect number!" - if the number is perfect.
# · "It's not so perfect." - if the number is NOT perfect.
# A perfect number is a positive integer that is equal to the sum of its proper positive divisors.
# That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
# input is 6 so n in range by 1 is in loops and count 6 times by 1, in conditions is checking the module of 6 and iterated
# number and is counting as a 1 + 2 + 3 and then is chekcing is equal or not if is it is perfect if not is not perfect