def calculation(operator, a, b):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        return a // b
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


input_operator = input()
first_num = int(input())
second_num = int(input())
print(calculation(input_operator, first_num, second_num))
# always fist the input about the quastion and then the integur which you will use to calculate