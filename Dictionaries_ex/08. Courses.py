command = input()

school_information = {}
while command != "end":
    course_name, student_name = command.split(" : ")
    school_information[course_name] = school_information.get(course_name, {})
    school_information[course_name][student_name] = student_name
    command = input()

for lang_is in school_information:
    print(f"{lang_is}: {len(school_information[lang_is])}")
    for key, value in school_information[lang_is].items():
        print(f"-- {value}")