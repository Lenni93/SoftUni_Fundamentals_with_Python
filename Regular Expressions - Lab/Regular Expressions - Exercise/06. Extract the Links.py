import re

pattern = re.compile(
    r"www.([A-Za-z0-9\-]+)(\.[a-z]+)+")

while True:
    string = input()
    if string:
        result = re.finditer(pattern, string)
        for show in result:
            print(show[0])
    else:
        break






#
#
#
# import re
# pattern = re.compile(r"\bwww\.[a-zA-Z0-9-]+\.[a-z]+(\.[a-z]+)*\b")
# while True:
#     string = input()
#     if string:
#         matches = pattern.finditer(string)
#         for show in matches:
#             print(show[0])
#     else:
#         break