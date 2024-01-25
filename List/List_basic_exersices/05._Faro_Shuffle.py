shuffle = input().split(",")
count = int(input())
middle_of_deck = len(shuffle) // 2

for i in range(count):
    if count % 3 != 0:
        list_.append(shuffle)
        check += list_
    elif count % 2 == 0:

