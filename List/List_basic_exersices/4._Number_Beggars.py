first_line = input().split(",")
beggars = int(input())

first_line = [int(first_line[i]) for i in range(len(first_line))]
beggar_total = []

for beggar in range(beggars):
    beggar_sum = []
    for index in range(beggar, len(first_line), beggars):
        beggar_sum.append(first_line[index])
    temp_sum = sum(beggar_sum)
    beggar_total.append(temp_sum)

print(beggar_total)