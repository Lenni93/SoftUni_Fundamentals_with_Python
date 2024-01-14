string_ = input()

while string_ != 'End':
    if string_ != 'SoftUni':
        [print(i * 2, end="") for i in string_]
        print()
    string_ = input()
# first we got Hello Word which words is repeated as a HHeelllloo WWoorrlldd then we got Repeate and is repeated
# RReeppeeaatt and in the end we received END. When is SoftUni is just passing and when is END the command is stopped
# You will be given strings until you receive the command "End". For each string given,
# you should print a string in which each character (case-sensitive) is repeated twice.
# Note that if you receive the string "SoftUni", you should NOT print it!