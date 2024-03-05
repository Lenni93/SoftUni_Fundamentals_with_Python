command = input()
students_dict = {}
while ":" in command:
    date = command.split(':')
    name, point, course = date[0], date[1], date[2]
    if course not in students_dict:
        students_dict[course] = {}
    students_dict[course][point] = name
    command = input()

course = ' '.join(command.split("_"))
for key, value in students_dict.items():
    if key == course:
        for point, name in value.items():
            print(f'{name} - {point}')
