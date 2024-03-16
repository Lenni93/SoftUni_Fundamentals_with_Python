sequence_of_string = input().split(" ")
result = ''
for word in sequence_of_string:
    length = len(word)
    result += length * word
print(result)

