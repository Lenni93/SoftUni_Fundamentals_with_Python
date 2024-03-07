n = int(input())
synonyms = {}
for count in range(n):
    name = input()
    synonym = input()
    if name not in synonyms:
        synonyms[name] = []
    synonyms[name].append(synonym)
for name in synonyms:
    print(f'{name} - {", ".join(synonyms[name])}')
