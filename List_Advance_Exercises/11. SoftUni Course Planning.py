schedule_of_lessons = input().split(", ")


def check_for_exercise(find_index: int) -> bool:
    try:
        return "Exercise" in schedule_of_lessons[find_index + 1]
    except IndexError:
        return


def add_lesson(lesson_title: str) -> None:
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)


def insert_lesson(lesson_title: str, index: int) -> None:
    if lesson_title not in schedule_of_lessons:
        schedule_of_lessons.insert(index, lesson_title)


def remove_lesson(lesson_title: str) -> None:
    if lesson_title in schedule_of_lessons:
        find_index = schedule_of_lessons.index(lesson_title)
        if check_for_exercise(find_index):
            del schedule_of_lessons[find_index]
        del schedule_of_lessons[find_index]


def swap_lesson(lesson_title: str, lesson_title_swap: str) -> None:
    if lesson_title in schedule_of_lessons and lesson_title_swap in schedule_of_lessons:
        index_lesson_one = schedule_of_lessons.index(lesson_title)
        index_lesson_two = schedule_of_lessons.index(lesson_title_swap)
        schedule_of_lessons[index_lesson_one], schedule_of_lessons[index_lesson_two] = \
            schedule_of_lessons[index_lesson_two], schedule_of_lessons[index_lesson_one]
        if check_for_exercise(index_lesson_one):
            schedule_of_lessons.insert(index_lesson_two + 1, schedule_of_lessons.pop(index_lesson_one + 1))
        if check_for_exercise(index_lesson_two):
            schedule_of_lessons.insert(index_lesson_one + 1, schedule_of_lessons.pop(index_lesson_two + 1))


def exercise_lesson(lesson_title: str) -> bool:
    if lesson_title in schedule_of_lessons:
        find_index = schedule_of_lessons.index(lesson_title)
        if not check_for_exercise(find_index):
            schedule_of_lessons.insert(find_index + 1, f"{lesson_title}-Exercise")
    elif lesson_title not in schedule_of_lessons:
        schedule_of_lessons.append(lesson_title)
        schedule_of_lessons.append(f"{lesson_title}-Exercise")


commands = {
    "Add": add_lesson,
    "Insert": insert_lesson,
    "Remove": remove_lesson,
    "Swap": swap_lesson,
    "Exercise": exercise_lesson
}

command = input()

while command != "course start":
    command_type, *info = [int(x) if x.isdigit() else x for x in command.split(":")]
    commands[command_type](*info)
    command = input()

for pos, lesson in enumerate(schedule_of_lessons, 1):
    print(f"{pos}.{lesson}")