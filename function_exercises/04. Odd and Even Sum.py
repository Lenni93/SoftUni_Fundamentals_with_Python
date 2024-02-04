def find_even_and_odd(n):
    even_number = 0
    odd_number = 0
    for num in range(len(number)):
        current_number = int(number[num])

        if current_number % 2 == 0:
            even_number += current_number
        else:
            odd_number += current_number
    return f"Odd sum = {odd_number}, Even sum = {even_number}"


number = input()
result = find_even_and_odd(number)
print(result)

# with loops we are calculate the len and then with condition statement we are checking which one is odd or even
# so in the end we sum it in the result
# input
# 1000435
# output
# Odd sum = 9, Even sum = 4
# You will receive a single number. You should write a function that returns the sum of all even and
# all odd digits in a given number. The result should be returned as a single string in the format:
# "Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
# Print the result of the function on the console.