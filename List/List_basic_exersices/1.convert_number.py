num_as_string = input()
num_as_list = num_as_string.split()
for i in range(len(num_as_list)):
    num_as_list[i] = - int(num_as_list[i])
print(num_as_list)
# len is checking number by number and -int is converting
# but is - and then will be + because - - = +
# split method is to split the numbers with comma
