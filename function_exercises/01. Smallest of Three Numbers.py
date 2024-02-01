def calculate(n1, n2, n3):
    smallest_sum = 0
    if n1 > n2 and n3 > n2:
        smallest_sum = n2
    elif n2 > n1 and n3 > n1:
        smallest_sum = n1
    elif n1 > n3 and n2 > n3:
        smallest_sum = n3
    return smallest_sum


first_num = int(input())
second_num = int(input())
third_num = int(input())
result = calculate(first_num, second_num, third_num)
print(result)



# Write a function that receives three integer numbers and returns the smallest.
# Print the result on the console. Use an appropriate name for the function.