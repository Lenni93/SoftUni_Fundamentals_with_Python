version = [int(digit) for digit in input().split(".")]
version[-1] += 1
for index in range(len(version) - 1, 0, -1):
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1
print(".".join(str(digit) for digit in version))

# with version[-1] += 1 we increase the last digit with one
# version[index] condition if is greater than 9
# version[index - 1] += 1
# version[index] = 0 the last digit become 0 and if the second digit is 9 then in the next loops will be 0