def date_types(types, n):
    result = ''
    if types == "int":
        result = f"{int(n) * 2:.0f}"
    elif types == 'real':
        result = f"{float(n) * 1.5:.2f}"
    elif types == 'string':
        result = "$" + n + "$"
    return result


same_char = input()
num = input()
print(date_types(same_char, num))