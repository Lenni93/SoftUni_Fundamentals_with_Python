# Create a class Zoo. It should have a class attribute called __animals that stores the total count of the animals
# in the zoo. The __init__ method should only receive the name of the zoo. There you should also create 3 empty lists
# (mammals, fishes, birds).
class Zoo:
    __animals = 0

    def __init__(self, name):
        self.zoo_name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    # The class should also have 2 more methods:
    # · add_animal(species, name) - based on the species, adds the name to the corresponding list
    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    # · get_info(species) - based on the species returns a string in the following format:
    # "{Species} in {zoo_name}: {names}
    # Total animals: {total_animals}"
    def get_info(self, species):
        result = []
        if species == 'mammal':
            result = self.mammals
            species = "Mammals"
        elif species == 'fish':
            result = self.fishes
            species = "Fishes"
        elif species == 'bird':
            result = self.birds
            species = "Birds"
        return f"{species} in {self.zoo_name}: {', '.join(result)} \nTotal animals: {Zoo.__animals}"


# On the first line, you will receive the name of the zoo. On the second line, you will receive number n.
zoo_name = input()
# Add the animal to the zoo to the corresponding list. The species could be "mammal", "fish", or "bird".
zoo = Zoo(zoo_name)
# On the following n lines you will receive animal info in the format:"{species} {name}".
number_n = int(input())
for i in range(number_n):
    type, current = input().split()
    zoo.add_animals(type, current)

info = input()
print(zoo.get_info(info))
