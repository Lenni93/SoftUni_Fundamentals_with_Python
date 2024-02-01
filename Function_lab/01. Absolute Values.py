sequence_number = input().split()
number_of_list = []
for n in sequence_number:
    number = float(n)
    number_of_list.append(number)
list_absolute_number = []
for n in number_of_list:
    absolute_number = abs(n)
    list_absolute_number.append(absolute_number)
print(list_absolute_number)
