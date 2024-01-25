count = int(input())
factor = int(input())
list_of_num = []
range_of = count * factor
for i in range(0, range_of, count):
    i += count
    list_of_num.append(i)
print(list_of_num)
