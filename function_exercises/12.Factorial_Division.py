import math

first_factorial = int(input())
second_factorial = int(input())


def factorial_division(num1, num2):
    num1 = math.factorial(num1)
    num2 = math.factorial(num2)
    return f"{(num1 / num2):.2f}"


print(factorial_division(first_factorial, second_factorial))

# Write a function that receives two integer numbers. Calculate the factorial of each number.
# Divide the first result by the second and print the division formatted to the second decimal point.
# factorial division of 5 is 120 so divided by 2 is 60
# Factorial division number of 6 is 720 so divided by 2  is 360
