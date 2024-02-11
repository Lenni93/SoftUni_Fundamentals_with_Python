first_sequences = input().split(', ')
second_sequences = input().split(', ')
substring = []
for first_check in first_sequences:
    for second_check in second_sequences:
        if first_check in second_check:
            substring.append(first_check)
            break

print(substring)
# first_check checking if the string has the same name as a: arp, live, strong and lively, alive, harp, sharp, armstrong
# from the first arp, live, strong  is in the second sequences harp,alive, armstrong.