def is_valid_input(input_string):
    if len(input_string.split(":")) != 2:
        return False
    name, title = input_string.split(":")

    if len(name) < 6 or name[0] != "|" or name[-1] != "|":
        return False
    name = name[1:-1]
    if not name.isupper():
        return False

    if len(title) < 7 or title[0] != "#" or title[-1] != "#" or title.count(" ") != 1:
        return False
    title = title[1:-1]
    words = title.split()
    if len(words) != 2 or not all(word.isalpha() for word in words):
        return False

    return True


num_input = int(input())
for _ in range(num_input):
    input_data = input()
    if is_valid_input(input_data):
        name, title = input_data.split(":")
        name = name[1:-1]
        title = title[1:-1]
        print(f"{name}, The {title}")
        print(f">> Strength: {len(name)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")

        # Create a program that checks if inputs are valid. On the first line, you will receive a number that indicates how many inputs you will receive on the following lines.
        #
        # You will read lines with a boss name and title, and you should check if they are valid, considering the following rules:
        # •	Boss - the name should be
        # o	In upper case letters
        # o	Minimum four letters long
        # o	Surrounded by "|"
        # •	Title – should:
        # o	It contains exactly 2 words, and they contain only alphabetical letters and 1 whitespace between them.
        # o	Surrounded by "#"
        # •	The name and title should be split by a single ":"
        # Example for a valid input:  |GEORGI|:#Lead architect#
        # If the input is valid. Print in the following format:
        #
        # "{boss name}, The {title}
        # >> Strength: {length of the name}
        # >> Armor: {length of the title}"
        #
        # If the input is invalid, print "Access denied!"