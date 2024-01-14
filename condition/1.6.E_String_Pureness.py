n = int(input())
symbols = ".,_"

for text in range(n):
    string_name = input()
    if any(x in string_name for x in symbols):
        print(f"{string_name} is not pure!")
    else:
        print(f"{string_name} is pure.")
# first checking is 2 times so the first one is 'pure string' which is with is pure because there is no characters,
# the second one is 'not_pure_string' which is with two characters "_" so is in not pure strings
# You will be given number n. After that, you'll receive different strings n times.
# Your task is to check if the given strings are pure, meaning that they do NOT consist of any of
# the characters: comma ",", period ".", or underscore "_":
# •	If a string is pure, print "{string} is pure."
# •	Otherwise, print "{string} is not pure!"