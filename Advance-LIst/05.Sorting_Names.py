read_name = input().split(', ')
sorted_name = sorted(read_name, key=lambda x: (-len(x), x))

print(sorted_name)

# Write a program that reads a single string with names separated by comma and space ", ". Sort
# the names by their length in descending order. If 2 or more names have the same length,
# sort them in ascending order (alphabetically). Print the resulting list.
# input: Ali, Marry, Kim, Teddy, Monika, John
# output: [' Monika', ' Marry', ' Teddy', ' John', ' Kim', 'Ali']
#  sorted(read_name, key=lambda x: (-len(x), x)) is reversed from the bigger amount till less length in descending order