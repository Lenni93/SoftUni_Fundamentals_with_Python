string = input()

while True:
    command = input()

    if command == "Done":
        break

    if command.startswith("Change"):
        char, replacement = command.split()[1], command.split()[2]
        string = string.replace(char, replacement)
        print(string)

    elif command.startswith("Includes"):
        substring = command.split()[1]
        if substring in string:
            print("True")
        else:
            print("False")

    elif command.startswith("End"):
        substring = command.split()[1]
        if string.endswith(substring):
            print("True")
        else:
            print("False")

    elif command == "Uppercase":
        string = string.upper()
        print(string)

    elif command.startswith("FindIndex"):
        char = command.split()[1]
        index = string.find(char)
        print(index)

    elif command.startswith("Cut"):
        start_index, count = int(command.split()[1]), int(command.split()[2])
        cut_string = string[start_index:start_index+count]
        print(cut_string)

        # Create a program that executes changes over a string. On the first line, you are going to receive the string. On the following lines, you will be receiving commands until the "Done" command. There are six possible commands:
        # •	"Change {char} {replacement}"
        # o	Replace all occurrences of the char with the given replacement, then print the string.
        # •	"Includes {substring}"
        # o	Check if the string includes the given substring with and print "True" or "False".
        # •	"End {substring}"
        # o	Check if the string ends with the given substring and print "True" or "False".
        # •	"Uppercase"
        # o	Make the whole string uppercased, then print it.
        # •	"FindIndex {char}"
        # o	Find the index of the first occurrence of the given char, then print it.
        # •	"Cut {startIndex} {count}"
        # o	Remove all characters from the string, except those starting from the given start index and the next count of characters. Print only the cut chars.
        # Input
        # •	On the first line, you are going to receive the string.
        # •	On the following lines, until the "Done" command is received, you will be receiving commands.
        # •	All commands are case-sensitive.
        # •	The input will always be valid.
        # Output
        # •	Print the output of every command in the format described above.