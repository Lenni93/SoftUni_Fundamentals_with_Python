number = int(input())
positive_list = []
negative = []
count_positive = 0
for _ in range(number):
    positive = int(input())
    if positive >= 0:
        positive_list.append(positive)
    else:
        negative.append(positive)
print(positive_list)
print(negative)
print(f"Count of positives: {len(positive_list)}")
print(f"Sum of negatives: {sum(negative)}")