command = input()
dict_resource = {}
while command != 'stop':
    point = int(input())
    dict_resource[command] = dict_resource.get(command, 0) + point
    command = input()

for odd, even in dict_resource.items():
    print(f'{odd} -> {even}')
