heroes = {}

while True:
    command = input().split()
    if command[0] == "Enroll":
        hero_name = command[1]
        if hero_name in heroes:
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []

    elif command[0] == "Learn":
        hero_name, spell_name = command[1], command[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name in heroes[hero_name]:
            print(f"{hero_name} has already learnt {spell_name}.")
        else:
            heroes[hero_name].append(spell_name)

    elif command[0] == "Unlearn":
        hero_name, spell_name = command[1], command[2]
        if hero_name not in heroes:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes[hero_name].remove(spell_name)

    elif command[0] == "End":
        break

print("Heroes:")
for hero, spells in heroes.items():
    print(f"== {hero}: {', '.join(spells)}")
# Create a program that keeps track of enrolled heroes and their collection of spells (spellbook).  You will be receiving the following commands until you receive the command "End":
# •	"Enroll {HeroName}":
# o	Adds the hero to your collection of heroes.
# o	If the hero is already present in your collection, print: "{HeroName} is already enrolled."
# •	"Learn {HeroName} {SpellName}":
# o	Adds the spell to the hero's spellbook.
# o	If the hero does not exist in the collection, print: "{HeroName} doesn't exist."
# o	If the hero already has the spell in his spellbook, print: "{HeroName} has already learnt {SpellName}."
# •	"Unlearn {HeroName} {SpellName}":
# o	Removes the spell from the hero's spellbook.
# o	If the hero doesn't exist in the collection, print: "{HeroName} doesn't exist."
# o	If the spell doesn't exist in the hero's spellbook, print: "{HeroName} doesn't know {SpellName}."
# o
# After receiving the "End" command, print all the heroes:
# "Heroes:
# == {name1}: {spell1}, {spell2}, {spelln}
# == {name2}: {spell1}, {spell2}, {spelln}
# …
# == {nameN}: {spell1}, {spell2}, {spelln}"
# Input / Constraints
# 	You will be receiving lines until you receive the "End" command.
# Output
# 	Print the heroes in the format described above.