# Now, let's assume the rectangle is just one of many shapes. Also, assume it
# is being drawn somewhere, so it needs other data attached to it - position,
# for example. Inheriting this from the Shape class makes things easier.

import math
from random import randint

class Shape:
    def __init__(self, position, color):
        self.position = position
        self.color = color

    def get_area(self):
        pass #All shapes will have an area, but it's meaningless to define here

    def get_perimeter(self):
        pass #Same as area

class Rectangle(Shape):
    def __init__(self, position, color, length, width):
        super(Rectangle, self).__init__(position, color)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * self.length + 2 * self.width

class Circle(Shape):
    def __init__(self, position, color, radius):
        super(Circle, self).__init__(position, color)
        self.radius = radius

    def get_area(self):
        return math.pi * (self.radius ** 2)

    def get_circumference(self):
        return math.pi * 2 * self.radius

    def get_perimeter(self): #Only called if the caller doesn't know which shape
        return self.get_circumference()

    
shape1 = Rectangle([1,2], 0x000000, 5, 4)
print(shape1.position)
print(shape1.get_area())

print()

shape2 = Circle([1,2], 0x000000, 5)
print(shape2.position)
print(shape2.get_area())

print()

shapes = [Rectangle([0, 0], 0x000000, 10, 4),
          Rectangle([50, 100], 0xFF0000, 10, 40),
          Circle([80, 400], 0x454545, 100),
          Circle([400, 80], 0x00FF00, 200)]

for shape in shapes:
    print("Name: " + type(shape).__name__)
    print("Area: " + str(shape.get_area()))
    print("Perimeter/Circumference: " + str(shape.get_perimeter()))
    print()

