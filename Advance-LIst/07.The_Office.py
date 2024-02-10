def check_employees_happiness():
    happiness_list = list(map(int, input().split()))
    employees_factor = int(input())

    improved_happiness = [happiness * employees_factor for happiness in happiness_list]
    average_happiness = sum(improved_happiness) / len(improved_happiness)
    happy_count = sum(happiness >= average_happiness for happiness in improved_happiness)
    total_count = len(improved_happiness)

    massage = 'are happy' if happy_count >= total_count / 2 else 'are not happy'
    result = f'Score: {happy_count}/{total_count}. Employees {massage}!'

    return result


print(check_employees_happiness())

# You will receive two lines of input:
# · a list of employees' happiness as a string of numbers separated by a single space
# · a happiness improvement factor (single number).
# Your task is to find out if the employees are generally happy in their office.
# First, multiply each employee's happiness by the factor.
# Then, print one of the following lines:
# · If half or more of the employees have happiness greater than or equal to the average:
# "Score: {happy_count}/{total_count}. Employees are happy!"
# · Otherwise:
# "Score: {happy_count}/{total_count}. Employees are not happy!"
