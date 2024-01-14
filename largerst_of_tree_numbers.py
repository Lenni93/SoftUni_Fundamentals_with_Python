fist_number = int(input())
second_number = int(input())
third_number = int(input())

if fist_number > second_number and fist_number > third_number:
    print(fist_number)
elif second_number > fist_number and second_number > third_number:
    print(second_number)
else:
    print(third_number)
