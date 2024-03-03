element = input().split(" ")
bakery = {}
for i in range(0, len(element), 2):
    key = element[i]
    value = int(element[i + 1])
    bakery[key] = value
print(bakery)




# element = input().split(" ")
# bakery = {}
# for i in range(0, len(element), 2):
#     key = element[i]
#     value = element[i + 1]
#     bakery[key] = int(value)
# print(bakery)


#using integer because from the task we should print int not string from the value