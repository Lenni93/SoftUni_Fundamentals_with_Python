number = int(input())
total = 0
for i in range(1, number + 1):
    for y in range(0, i):
        print('*', end='')
    print()

for i in range(number - 1, 0, -1):
    for y in range(0, i):
        print('*', end='')
    print()
# fist loop is start with 1 + 1 then always add by one
# next loops is from 5 then less by one
