def even_numbers(n):
    return n % 2 == 0


numbers = [int(number) for number in input().split()]

result = filter(even_numbers, numbers)
print(list(result))

# Write a program that receives a sequence of numbers (integers) separated by a single space.
# It should print a list of only the even numbers. Use filter().
