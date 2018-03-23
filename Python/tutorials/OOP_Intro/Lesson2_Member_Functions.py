# This adds the ability for the class to compute its own area and perimeter on
# demand - whoever wants the answer doesn't have to know the formula.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def getArea(self):
        return self.length * self.width
    
    def getPerimeter(self):
        return 2 * self.length + 2 * self.width

rect1 = Rectangle(5, 10)
print(rect1.getArea())


