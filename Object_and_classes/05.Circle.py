# Create a class Circle. In the __init__ method, the circle should only receive one parameter - its diameter.
# Create a class attribute called __pi that is equal to 3.14. The class should also have the following methods:
class Circle():
    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2
    # calculate_circumference() - returns the circumference of the circle
    # calculate_area() - returns the area of the circle
    # · calculate_area_of_sector(angle) - gives the central angle in degrees, returns the area that fills the sector


def calculate_circumference(self):
    return Circle.__pi * self.diameter


def calculate_area(self):
    return Circle.__pi * self.radius * self.radius


def calculate_area_of_sector(self, angle):
    return (angle / 360) * Circle.__pi * self.radius * self.radius


circle = Circle(10)

angle = 5

print(f"{circle.calculate_circumference():.2f}")

print(f"{circle.calculate_area():.2f}")

print(f"{circle.calculate_area_of_sector(angle):.2f}")

# diameter = 10 / 2
# radius = 5
# 3.14 * 10 * 2 x 5
# 78.50
# 5/360 * 3.14 * 25 = 1.0902..
