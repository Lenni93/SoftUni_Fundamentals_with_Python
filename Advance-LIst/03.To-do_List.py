notes = [0] * 10
while True:
    command = input()
    if command == "End":
       break
    words = command.split("-")
    priority = int(words[0]) - 1
    note = words[1]
    notes.pop(priority)
    notes.insert(priority, note)

result = [element for element in notes if element != 0]
print(result)



# priority = int(words[0] - 1 is removing from 2-Walk the dog and is 1 for now
# drink a coffee is 1 and from priority is taking 1 and is sort of 0 position