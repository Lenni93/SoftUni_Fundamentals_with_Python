name = input()
going_to = {
    "Gryffindor": 5,
    "Slytherin": 6,
    "Ravenclaw": 7,
    "Hufflepuff": 100
}

while name != "Welcome!":
    if name == "Voldemort":
        print("You must not speak of that name!")
        break
    for destination, num in going_to.items():
        if len(name) < num:
            print(f"{name} goes to {destination}.")
            break
    name = input()
else:
    print("Welcome to Hogwarts.")
# less than 5 is Gryffindor,if the name is exactly 5 is  Stytherin, less than 7 is ravenclaw and less than 100
# is Hufflepuff
# Help out the sorting hat to sort the new students in the houses of Hogwarts. You will be receiving names
# until the command "Welcome!". The length of each name determines in which house the student is going:
# •	If the name is less than 5 chars, the student is going into Gryffindor
# o	Print "{name} goes to Gryffindor."
# •	If the name is exactly 5 chars, the student is going into Slytherin
# o	Print "{name} goes to Slytherin."
# •	If the name is exactly 6 chars, the student is going into Ravenclaw
# o	Print "{name} goes to Ravenclaw."
# •	If the name is more than 6 chars, the student is going into Hufflepuff
# o	Print "{name} goes to Hufflepuff."
# While receiving names, if you receive "Voldemort", print "You must not speak of that name!"
# and end the program. No more sorting for today!
# If all students are sorted successfully, print "Welcome to Hogwarts.
