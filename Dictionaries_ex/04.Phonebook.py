phonebook = input()
dict_num = {}
while not phonebook.isdigit():
    name, number = phonebook.split("-")
    dict_num[name] = dict_num.get(name, number)
    phonebook = input()

for _ in range(int(phonebook)):
    name_check = input()
    if name_check in dict_num:
        print(f"{name_check} -> {dict_num[name_check]}")
    else:
        print(f"Contact {name_check} does not exist.")
