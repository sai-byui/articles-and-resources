# Just a really simple one, acts more or less like a C++ struct - only has
# member variables. This allows you to put two (or more) related pieces of
# information into the same container.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width


rect1 = Rectangle(6, 5)

print(rect1.length)
print(rect1.width)