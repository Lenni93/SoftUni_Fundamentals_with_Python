text = input().replace(" ", "")
char_text = {}

for char in text:

    if char not in char_text:
        char_text[char] = 0
    char_text[char] += 1

for key, value in char_text.items():
    print(f"{key} -> {value}")
