people = int(input())
wagon = list(map(int, input().split(' ')))
no_more_people = False
for spots in range(len(wagon)):
    while wagon[spots] < 4:
        wagon[spots] += 1
        people -= 1
        if people == 0:
            no_more_people = True
            break
    if no_more_people:
        break

if people == 0 and wagon[-1] == 4:
    print(*wagon)
elif people == 0:
    print("The lift has empty spots")
    print(*wagon)
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*wagon)


# from 15 taking 4 people till is less then 4