money_as_string = input().split(", ")
numbers_of_beggar = int(input())
money_as_integer = []
for current_money in money_as_string:
    money_as_integer.append(int(current_money))
final_sum = []
start_index = 0
while start_index < numbers_of_beggar:
    current_beggar_sum = 0
    for current_index in range(start_index, len(money_as_string), numbers_of_beggar):
        current_beggar_sum += money_as_integer[current_index]
    final_sum.append(current_beggar_sum)
    start_index += 1
print(final_sum)
# 100, 94, 24, 99
# 2
# [124, 193]
