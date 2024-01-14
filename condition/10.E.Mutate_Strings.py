first_string = input()
second_string = input()

for index in range(len(first_string)):
    if first_string[index] != second_string[index]:
        first_string = second_string[:index + 1] + first_string[index + 1:]
        print(first_string)

# first_text = [n for n in input()]
# second_text = [n for n in input()]
# target_list = list(first_text)
# for index, (letter_a, letter_b) in enumerate(zip(first_text, second_text)):
#     if letter_a != letter_b:
#         target_list[index] = letter_b
#         for letter in target_list:
#             print(f"{letter}", end="")
#         print()


# transform first word of bubble gum to turtle gum just taking the first word of sentences  into the second
# You will be given two strings. Transform the first string into the second one,
# letter by letter, starting from the first anyone. After each interaction,
# print the resulting string only if it is unique.
# Note: the strings will have the same length.