string_ = input()

needed_coffee = 0
event = ['coding', 'dog', 'cat', 'movie']
while string_ != 'END':
    if string_.lower() in event:
        if string_ in event:
            needed_coffee += 1
        else:
            needed_coffee += 2
    string_ = input()

if needed_coffee > 5:
    print('You need extra sleep')
else:
    print(needed_coffee)

# when is uppercase is + 2 so we've got only once per first checking and is it 1 + 2 = 3
# the first once is with lowercase which we are ignore and the second one is with uppercase and the third one is with
# uppercase, so it will be like 1 + 2 and the forth once is also with uppercase and it will be 3 + 2 = 5
# Everybody knows that you spend too much time awake during nighttime.
# Your task is to define how much coffee you need to stay awake.
# Until you receive the command "END", you need to read commands on different lines.
# According to the commands, calculate the number of coffees you need to drink to stay awake
# during the daytime.
# The list of events can contain the following:
# •	You have homework to do ("coding").
# •	You have a dog or a cat that decided to wake you up too early ("dog" or "cat").
# •	You watch a movie ("movie").
# •	If other events are present, they will be represented by arbitrary strings. Just ignore them!
# Each event can be lowercase or uppercase:
# •	If it is lowercase, you need 1 coffee by an event.
# •	If it is uppercase, you need 2 coffees by an event.
# In the end, print the number of coffees you will need.
# If the count has exceeded 5, just print "You need extra sleep".