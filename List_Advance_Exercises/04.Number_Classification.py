def positive_numbers(list_of_number):
    return ', '.join([number for number in list_of_number if int(number) >= 0])


def negative_numbers(list_of_number):
    return ', '.join([number for number in list_of_number if int(number) < 0])


def even_numbers(list_of_number):
    return ', '.join([number for number in list_of_number if int(number) % 2 == 0])


def odd_numbers(list_of_number):
    return ', '.join([number for number in list_of_number if int(number) % 2 != 0])


numbers = input().split(", ")

print(f'Positive: {positive_numbers(numbers)}')
print(f'Negative: {negative_numbers(numbers)}')
print(f'Even: {even_numbers(numbers)}')
print(f'Odd: {odd_numbers(numbers)}')

#
# Using a list comprehension, write a program that receives numbers, separated by comma and space ", ",
# and prints all the positive, negative, even, and odd numbers on separate lines as shown below.
#
# Note: Zero is counted as a positive number