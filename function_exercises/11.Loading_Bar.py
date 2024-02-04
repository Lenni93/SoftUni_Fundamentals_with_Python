numbers = int(input())

def loading_bar(n):
    num_range = int(n / 10)
    target = 10
    if target == num_range:
        return "100% Complete!\n" "[" + target * "%" + "]"
    else:
        return f"{n}% " + "[" + num_range * "%" + (target - num_range) * "." + "]\n" + "Still loading..."


print(loading_bar(numbers))


# You will receive a single integer number between 0 and 100 (inclusive) divisible by 10 without remainder
# (0, 10, 20, 30...). Your task is to create a function that returns a loading bar depending on the number
# you have received in the input. Print the result on the console. For more clarification, see the examples below.
# input: 30
# output:
# 30% [%%%.......] Still loading...
# input: 100
#output:
#100% Complete! [%%%%%%%%%%]