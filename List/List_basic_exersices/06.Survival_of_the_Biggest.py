string_of_integer = input().split()
count = int(input())
list_of_integer = []
for current_count in string_of_integer:
    list_of_integer.append(int(current_count))
for _ in range(count):
    list_of_integer.remove(min(list_of_integer))
print(*list_of_integer, sep=", ")
