name_char = input().split(", ")
chars = {word: ord(word) for word in name_char}
print(chars)




# a, b, c, a
# output{'a': 97, 'b': 98, 'c': 99}