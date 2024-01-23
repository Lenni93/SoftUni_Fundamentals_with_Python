n = int(input())
command_ = {
    "odd": [],
    "even": [],
    "negative": [],
    "positive": []

}
for i in range(n):
    current_number = int(input())
    if current_number % 2 != 0:
        command_["odd"].append(current_number)
    if current_number % 2 == 0:
        command_["even"].append(current_number)
    if current_number >= 0:
        command_["positive"].append(current_number)
    else:
        command_["negative"].append(current_number)


print(command_[input()])

# numbers = [int(input()) for _ in range(int(input()))]
# command = input()
# print([x for x in numbers if any([command == "odd" and x % 2 != 0,
# command == "even" and x % 2 ==0,command == "positive" and x >= 0, command == "negative" and x < 0])])