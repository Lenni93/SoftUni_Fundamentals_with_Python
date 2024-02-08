even_number = list(map(int, input().split(', ')))
checking_num = [even for even in range(len(even_number)) if even_number[even] % 2 == 0]

print(checking_num)