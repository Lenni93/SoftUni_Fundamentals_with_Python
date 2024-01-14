positive_number = float(input())
if positive_number == 0:
    print("zero")
elif positive_number > 0:
    if positive_number < 1:
        print("small positive")
    elif positive_number > 1000000:
        print("large positive")
    else:
        print("positive")
else:
    if abs(positive_number) < 1:
        print("small negative")
    elif abs(positive_number) > 1000000:
        print("large negative")
    else:
        print("negative")
        