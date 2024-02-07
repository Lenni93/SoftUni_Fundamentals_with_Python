text = input()
no_vowels = [x for x in text if x.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(no_vowels))
# comprehenstion