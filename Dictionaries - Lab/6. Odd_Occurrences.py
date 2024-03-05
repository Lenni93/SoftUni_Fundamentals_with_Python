odd_number = input().split(" ")
checks = {}
for odd in odd_number:
    odd = odd.lower()
    if odd not in checks:
        checks[odd] = 0
    checks[odd] += 1
for key, value in checks.items():
    if value % 2 != 0:
        print(key, end=" ")
