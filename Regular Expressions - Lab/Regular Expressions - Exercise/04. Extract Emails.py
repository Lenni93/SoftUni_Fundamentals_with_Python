import re
string = input()

pattern = re.compile(
    r"(^|(?<=\s))([A-Za-z0-9])+([\.\-\_][A-Za-z0-9]+)*@([A-Za-z-]+)\.([A-Za-z-]+)([\.A-Za-z-])*(\b|(?=\s))")
result = re.finditer(pattern, string)
for show in result:
    print(show[0])








#
#
# import re
# string = input()
# pattern = re.compile(r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))")
# matches = pattern.finditer(input_string)
#
# for show in matches:
#     print(show[0])