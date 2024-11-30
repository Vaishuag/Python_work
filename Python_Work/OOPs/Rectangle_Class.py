import math

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)

    def diagonal(self):
        return math.sqrt(self.length ** 2 + self.breadth ** 2)

rect = Rectangle(5, 12)
print("Area of Rectangle:", rect.area())            
print("Perimeter of Rectangle:", rect.perimeter())  
print("Diagonal of Rectangle:", round(rect.diagonal(), 2))  
